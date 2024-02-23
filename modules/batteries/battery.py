from typing import Any
from database.model import get_single_battery_by_code, update_battery, create_request_log
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import json_loader

def process_battery_request(db: Session, data: Any):
    create_request_log(db=db, server_type="battery", name="post", value=str(data))
    if isinstance(data, bytes) == False:
        return {
            's': 0,
            'h': 0,
            'sh': 0,
        }
    else:
        data = data.decode()
        jdata = json_loader(jstr=data)
        if jdata is None:
            return {
                's': 0,
                'h': 0,
                'sh': 0,
            }
        else:
            if type(jdata) is not dict:
                return {
                    's': 0,
                    'h': 0,
                    'sh': 0,
                }
            else:
                jlist = list(jdata.keys())
                clist = ['t', 'c', 'v', 'bID', 'SOC', 's', 'LT', 'LG']
                check =  all(item in jlist for item in clist)
                if check is False:
                    return {
                        's': 0,
                        'h': 0,
                        'sh': 0,
                    }
                else:
                    battery = get_single_battery_by_code(db=db, code=str(jdata['bID']))
                    if battery is None:
                        return {
                            's': 0,
                            'h': 0,
                            'sh': 0,
                        }
                    else:
                        values = {
                            'voltage': jdata['v'],
                            'temperature': jdata['t'],
                            'charge': jdata['SOC'],
                            'electric_current': jdata['c'],
                            'latitude': jdata['LT'],
                            'longitude': jdata['LG'],
                        }
                        b_status = jdata['s']
                        is_shutdown = 0
                        is_hotlisted = 0
                        if battery.status == 2:
                            is_shutdown = 1
                        elif battery.status == 4:
                            is_hotlisted = 1
                        else:
                            values['status'] = jdata['s']
                        update_battery(db=db, id=battery.id, values=values)
                        return {
                            's': 1,
                            'h': is_hotlisted,
                            'sh': is_shutdown,
                        }
                        