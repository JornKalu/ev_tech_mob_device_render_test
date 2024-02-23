from fastapi import APIRouter, Request, Depends, HTTPException
from database.db import get_session
from sqlalchemy.orm import Session
from modules.mobility_devices.mob_dev import get_mobility_device, sync_mobility_device, start_mobility_device, stop_mobility_device
from database.schema import MobilityDeviceModel, ErrorResponse, SyncMobDeviceModel, SyncMobDeviceResponseModel, MobDevActionModel, MobDevActionResponseModel

router = APIRouter(
    prefix="/mobility_device",
    tags=["v1_mobility_device"]
)

@router.get("/by_id/{mobility_device_id}", response_model=MobilityDeviceModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def by_id(db: Session = Depends(get_session), mobility_device_id: int = 0):
    return get_mobility_device(db=db, mobility_device_id=mobility_device_id)

@router.post("/sync", response_model=SyncMobDeviceResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def sync(fields: SyncMobDeviceModel, db: Session = Depends(get_session)):
    original_values = fields.model_dump_json()
    req = sync_mobility_device(db=db, mobility_device_id=fields.mobility_device_id, initial_instruction=fields.initial_instruction, original_values=original_values, latitude=fields.latitude, longitude=fields.longitude, charge=fields.charge, speed=fields.speed)
    return req

@router.post("/start", response_model=MobDevActionResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def start(fields: MobDevActionModel, db: Session = Depends(get_session)):
    req = start_mobility_device(db=db, mobility_device_id=fields.mobility_device_id)
    return req

@router.post("/stop", response_model=MobDevActionResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def stop(fields: MobDevActionModel, db: Session = Depends(get_session)):
    req = stop_mobility_device(db=db, mobility_device_id=fields.mobility_device_id)
    return req