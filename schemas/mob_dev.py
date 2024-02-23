from typing import Optional
from pydantic import BaseModel
from schemas.battery import BatteryModel

class MobilityDeviceModel(BaseModel):
    id: int
    user_id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    device_type_id: Optional[int] = None
    model: Optional[str]
    registration_number: Optional[str] = None
    vin: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    conversion_date: Optional[str] = None
    front_image: Optional[str] = None
    left_image: Optional[str] = None
    right_image: Optional[str] = None
    back_image: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[str] = None
    type_name: Optional[str] = None
    type_code: Optional[str] = None
    type_description: Optional[str] = None
    number_of_wheels: Optional[int] = None
    number_of_batteries: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    customer_full_name: Optional[str] = None
    customer_address: Optional[str] = None
    created_by: Optional[str] = None
    batteries: Optional[BatteryModel] = None

    class Config:
        orm_mode = True

class SyncMobDeviceModel(BaseModel):
    mobility_device_id: int
    initial_instruction: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    charge: Optional[str] = None
    speed: Optional[str] = None
    # status: Optional[int] = None

    class Config:
        orm_mode = True

class SyncMobDeviceDataModel(BaseModel):
    status: Optional[int] = None

    class Config:
        orm_mode = True

class SyncMobDeviceResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[SyncMobDeviceDataModel] = None

    class Config:
        orm_mode = True

class MobDevActionModel(BaseModel):
    mobility_device_id: int

    class Config:
        orm_mode = True

class MobDevActionResponseModel(BaseModel):
    status: bool
    message: str

    class Config:
        orm_mode = True