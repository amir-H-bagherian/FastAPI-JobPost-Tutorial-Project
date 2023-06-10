from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str  
    
class UserResponseSchema(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True