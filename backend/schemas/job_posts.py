from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url = Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    
def JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str
    
def JobShow(JobBase):
    title: str
    company: str
    company_url = Optional[str]
    location: str
    description: Optional[str]
    date_posted: date