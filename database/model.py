from typing import Dict
from models.admins import Admin, create_admin, update_admin, delete_admin, get_single_admin_by_id, get_admins
from models.batteries import Battery, create_battery, update_battery, delete_battery, get_single_battery_by_id, get_single_battery_by_code, get_all_batteries, get_all_batteries_by_mobility_device_id, search_batteries, count_batteries, count_batteries_by_code, check_if_battery_code_exists
from models.collections import Collection, create_collections, update_collection, delete_collection, get_single_collection_by_id, get_all_collections
from models.logs import Log, create_log, update_log, delete_log, get_single_log_by_id, get_logs_by_user_id, get_logs_by_user_id_and_status, get_logs_by_station_id, get_logs_by_station_id_and_status, get_logs_by_mobility_device_id, get_logs_by_mobility_device_id_and_status, get_logs_by_user_device_id, get_logs_by_user_device_id_and_status, get_all_logs, count_logs
from models.mobility_device_types import Mobility_Device_Type, create_mobility_device_type, update_mobility_device_type, delete_mobility_device_type, get_single_mobility_device_type_by_id, get_all_mobility_device_types, count_mobility_device_types
from models.mobility_devices import Mobility_Device, create_mobility_device, update_mobility_device, delete_mobility_device, get_single_mobility_device_by_id, get_all_user_mobility_device, get_single_mobility_devices_by_user_id, get_single_mobility_devices_by_user_id_and_status, get_single_mobility_devices_by_type, get_single_mobility_devices_by_type_id_and_status, get_single_mobility_devices_by_status, get_all_mobility_devices, search_mobility_devices, count_mobility_devices
from models.profiles import Profile, create_profile, update_profile, update_profile_by_user_id, delete_profile, get_profile_by_user_id
from models.request_logs import Request_Log, create_request_log, update_request_log, get_single_request_log_by_id, get_all_request_logs, count_request_logs
from models.users import User, create_user, update_user, delete_user, get_single_user_by_id, get_single_user_by_username, get_single_user_by_phone_number, get_single_user_by_email, get_users
import string
import random

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
