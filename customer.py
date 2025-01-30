from database import get_session
from models import Customer
from fastapi import FastAPI, APIRouter
from sqlmodel import Session
router = APIRouter(prefix="/customers",tags=["customer"])

@router.post("/signup")
def create_cus():
    pass

# @router.get()
# def read_cus():
#     pass
#
# @router.put()
# def update_cus():
#     pass
#
# @router.delete()
# def delete_cus():
#     pass