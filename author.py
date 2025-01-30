from typing import Annotated

from sqlmodel import Field
from database import get_session
from models import Author, User, Userpropety
from fastapi import FastAPI, APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import  AsyncSession
from sqlmodel import Session, select

# class authorout(Author):
#     id:int= Field()

router = APIRouter(prefix="/authors", tags=["author"])

@router.get("/")
async def read_authors( dbsession:AsyncSession=Depends(get_session)):
    statement = select(Author)
    sqlauthors = await dbsession.execute(statement)
    authors = sqlauthors.scalars().all()
    # json_books = [row.model_dump() for row in books]
    return authors

# @router.post("/signup")
# async def create_auth(authorinf: Userpropety , db:AsyncSession=Depends(get_session)):
#     statment : str = f"INSERT INTO author (flname) VALUE ({authorinf.flname})"
#     result = await session.exec(INSERT INTO(author (flname) VALUE authorinf.flname))
#     session.add(authorinf)
#     await session.commit()
#     await session.reset(authorinf)
#     return "jejeje"
    # pass

# @router.get()
# def read_auth():
#     pass


# @router.put()
# def update_auth():
#     pass
#
#
# @router.delete()
# def delete_auth():
#     pass