from fastapi import APIRouter, Request, Depends, HTTPException
from database.db import get_session
from sqlalchemy.orm import Session
from modules.batteries.battery import process_battery_request

router = APIRouter(
    prefix="/battery",
    tags=["v1_bat"]
)

# @router.post("/sync")
# async def post_requests(request: Request, db: Session = Depends(get_session)):
#     body = await request.body()
#     return process_battery_request(db=db, data=body)