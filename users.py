from datetime import datetime

from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from database import get_session
from models import Userpropety, User, Author, BookProperty, Book, Bookcreate, Genre

router = APIRouter(prefix="/users",tags=["user"])

@router.post("/signup",response_model=User)
async def creat_user(userinfo: Userpropety , dbsession:AsyncSession=Depends(get_session))-> User:
    db_user = User.model_validate(userinfo)
    dbsession.add(db_user)
    await dbsession.commit()
    await dbsession.refresh(db_user)
    if userinfo.role == "author":
        db_author = Author(user_id = db_user.id)

        dbsession.add(db_author)
        await dbsession.commit()
        await dbsession.refresh(db_author)
    return db_user


    # if userinfo.role == "author":
    #     db_author = Author(user_id = db_user.id)
    #     dbsession.add(db_author)
    #     await dbsession.commit()
    #     await dbsession.refresh(db_author)
# @router.get()
# def read(db: AsyncSession=Depends(get_session())):
#     pass
