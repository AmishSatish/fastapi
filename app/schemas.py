from datetime import datetime
from pydantic import BaseModel,EmailStr,validator
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut

    class Config:
        orm_mode=True

class PostOut(BaseModel):
    Post:Post
    votes:int

    class Config:
        orm_mode=True


class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str] = None

# class DirZeroOrOneError(Exception):
#     def __init__(self,message:str)->None:
#         self.message=message
#         super().__init__(message)

class Vote(BaseModel):
    post_id:int
    dir:int #conint(le=1)

    @validator('dir')
    @classmethod
    def isDirZeroOrOne(cls,value):
        if value not in [0,1]:
            # raise DirZeroOrOneError("Invalid value for dir")
            raise ValueError("Incorrect dir value")
        return value