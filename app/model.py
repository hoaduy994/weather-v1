from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from .DatabaseConnection import base

class Weather(base):
    __tablename__="info"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(255),unique=True,index=True)
    ip=Column(String(255),unique=True,index=True)
    time=Column(String(255),unique=True,index=True)