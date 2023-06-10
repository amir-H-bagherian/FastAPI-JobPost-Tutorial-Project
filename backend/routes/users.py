from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from schemas.users import UserCreateSchema, UserResponseSchema
from db.session import get_db
from crud.users import create_new_user


user_router = APIRouter(prefix='/users', tags=['users'])

@user_router.post('/', response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    new_user = create_new_user(db=db, user=user)
    return new_user