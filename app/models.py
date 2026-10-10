
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

from pydantic import BaseModel, ConfigDict


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    category = Column(String(200), nullable=False)
    level = Column(String(50), nullable=False)


class CourseCreate(BaseModel):
    title: str
    category: str
    level: str


class CourseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    category: str
    level: str

class CourseUpdate(BaseModel):
    title:str|None=None
    category:str|None=None
    level:str|None=None

class Resource(BaseModel):
    title: str
    platform: str
    url: str


class ResourceCreate(BaseModel):
    title: str
    platform: str
    url: str


class ResourceResponse(BaseModel):
    id: int
    title: str
    platform: str
    url: str