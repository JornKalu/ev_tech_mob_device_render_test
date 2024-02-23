from typing import Optional
from pydantic import BaseModel

class CreateBatteryModel(BaseModel):
    code: str
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class BatteryModel(BaseModel):
    id: int
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    voltage: Optional[str] = None
    temperature: Optional[str] = None
    charge: Optional[str] = None
    humidity: Optional[str] = None
    electric_current: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    status: Optional[int] = 0
    created_by: int
    created_at: str

    class Config:
        orm_mode = True

class CreateBatteryResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[BatteryModel] = None

    class Config:
        orm_mode = True

class UpdateBatteryModel(BaseModel):
    code: Optional[str] = None
    status: Optional[int] = None

    class Config:
        orm_mode = True

class GeneralBatteryResponseModel(BaseModel):
    status: bool
    message: str

    class Config:
        orm_mode = True
        