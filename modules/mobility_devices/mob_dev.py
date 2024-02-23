from typing import Any
from database.model import get_single_mobility_device_by_id, get_all_batteries_by_mobility_device_id, update_mobility_device, create_request_log, update_battery, update_request_log
from sqlalchemy.orm import Session
import json

def get_mobility_device(db: Session, mobility_device_id: int = 0):
    mobility_device = get_single_mobility_device_by_id(db=db, id=mobility_device_id)
    if mobility_device is None:
        return {
            'status': False,
            'message': 'Mobility device not found',
            'data': None,
        }
    else:
        batteries = get_all_batteries_by_mobility_device_id(db=db, mobility_device_id=mobility_device_id)
        data = {
            'id': mobility_device.id,
            'user_id': mobility_device.user_id,
            'code': mobility_device.code,
            'name': mobility_device.name,
            'device_type_id': mobility_device.device_type_id,
            'model': mobility_device.model,
            'registration_number': mobility_device.registration_number,
            'vin': mobility_device.vin,
            'latitude': mobility_device.latitude,
            'longitude': mobility_device.longitude,
            'conversion_date': mobility_device.conversion_date,
            'front_image': mobility_device.front_image,
            'left_image': mobility_device.left_image,
            'right_image': mobility_device.right_image,
            'back_image': mobility_device.back_image,
            'status': mobility_device.status,
            'created_at': mobility_device.created_at,
            'type_name': mobility_device.type_name,
            'type_code': mobility_device.type_code,
            'type_description': mobility_device.type_description,
            'number_of_wheels': mobility_device.number_of_wheels,
            'number_of_batteries': mobility_device.number_of_batteries,
            'username': mobility_device.username,
            'email': mobility_device.email,
            'phone_number': mobility_device.phone_number,
            'customer_full_name': mobility_device.customer_full_name,
            'customer_address': mobility_device.customer_address,
            'created_by': mobility_device.created_by,
            'batteries': batteries,
        }
        return {
            'status': True,
            'message': 'Success',
            'data': data,
        }

def sync_mobility_device(db: Session, mobility_device_id: int = 0, status: int = None, initial_instruction: str = None, original_values: str = None, latitude: str = None, longitude: str = None, charge: str = None, speed: str = None):
    req = create_request_log(db=db, initial_instruction=initial_instruction, server_type="mobility_device", name="post", value=original_values)
    mobility_device = get_single_mobility_device_by_id(db=db, id=mobility_device_id)
    if mobility_device is None:
        fin_data = {
            'status': False,
            'message': 'Mobility device not found',
            'data': None,
        }
        update_request_log(db=db, id=req.id, values={'response_value': json.dumps(fin_data)})
        return fin_data
    else:
        data = {
            'status': None,
        }
        val = {}
        if status is not None:
            val['status'] = status
            data['status'] = status
        if latitude is not None:
            val['latitude'] = latitude
        if longitude is not None:
            val['longitude'] = longitude
        if charge is not None:
            val['charge'] = charge
        if speed is not None:
            val['speed'] = speed
        update_mobility_device(db=db, id=mobility_device_id, values=val)
        fin_data = {
            'status': True,
            'message': 'Success',
            'data': data
        }
        update_request_log(db=db, id=req.id, values={'response_value': json.dumps(fin_data)})
        return fin_data

def start_mobility_device(db: Session, mobility_device_id: int = 0):
    mobility_device = get_single_mobility_device_by_id(db=db, id=mobility_device_id)
    if mobility_device is None:
        return {
            'status': False,
            'message': 'Mobility device not found',
            'data': None,
        }
    else:
        batteries = get_all_batteries_by_mobility_device_id(db=db, mobility_device_id=mobility_device_id)
        if len(batteries) > 0:
            for i in range(len(batteries)):
                battery = batteries[i]
                update_battery(db=db, id=battery.id, values={'temp_status': 1})
        update_mobility_device(db=db, id=mobility_device_id, values={'status': 1})
        return {
            'status': True,
            'message': 'Success',
        }
    
def stop_mobility_device(db: Session, mobility_device_id: int = 0):
    mobility_device = get_single_mobility_device_by_id(db=db, id=mobility_device_id)
    if mobility_device is None:
        return {
            'status': False,
            'message': 'Mobility device not found',
            'data': None,
        }
    else:
        batteries = get_all_batteries_by_mobility_device_id(db=db, mobility_device_id=mobility_device_id)
        if len(batteries) > 0:
            for i in range(len(batteries)):
                battery = batteries[i]
                update_battery(db=db, id=battery.id, values={'temp_status': 0})
        update_mobility_device(db=db, id=mobility_device_id, values={'status': 0})
        return {
            'status': True,
            'message': 'Success',
        }