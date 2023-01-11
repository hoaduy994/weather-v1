from dataclasses import Field
from fastapi import FastAPI, Request, Form
import requests
from typing import Optional, Union
from pydantic import BaseModel
from datetime import datetime
import uvicorn
from sqlalchemy import create_engine
from app.DatabaseConnection import engine,sessionLocal,base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import Session

app = FastAPI()

base.metadata.create_all(bind=engine)

class Item(BaseModel):
    q: Union[str, None] = None
    
class InfoSchema(BaseModel):
    id:int
    name:str
    ip:str
    time:str
    
    class Config:
        orm_model=True   
        
class Weather(base):
    __tablename__="info0"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(255),unique=True,index=True)
    ip=Column(String(255),unique=True,index=True)
    time=Column(String(255),unique=True,index=True)
         
@app.put('/weather')
async def search_city(infoSchema: InfoSchema, request: Request, q: str | None = None):
    API_KEY = '271d1234d3f497eed5b1d80a07b3fcd1' 
    city = q

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    
    response = requests.get(url).json()
    client_host = request.client.host
    start_date = datetime.today()
    temperature = response.get('main', {}).get('temp')
    description = response.get('weather', {})[0].get('description')
    
    info = Weather(id=infoSchema.id, name=city, ip = client_host, time= start_date)
    with Session(bind=engine) as session:
        session.add(info)
        session.commit() 
        
    if temperature:
        current_temperature = round(temperature - 273.15, 2)
        return f'Temperature of {city.title()} is {current_temperature}`C, description: {description}, IP is {client_host}, time is {start_date}' 
 
@app.get("/")
def home():
    return {"message": "The Weather!"}
        
if __name__ == '__main__':
    uvicorn.run("main:app")
    