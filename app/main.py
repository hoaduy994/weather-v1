from fastapi import FastAPI, Request, Form
import requests
from typing import Union
from pydantic import BaseModel
from datetime import datetime
import uvicorn
from sqlalchemy import create_engine
from app.DatabaseConnection import engine
from sqlalchemy.orm import Session
from . import model

app = FastAPI()

model.base.metadata.create_all(bind=engine)

class Item(BaseModel):
    q: Union[str, None] = None
    
class InfoSchema(BaseModel):
    id:int
    name:str
    ip:str
    time:str
    
    class Config:
        orm_model=True   
         
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
    
    info = model.Weather(id=infoSchema.id, name=city, ip = client_host, time= start_date)
    with Session(bind=engine) as session:
        session.add(info)
        session.commit() 
        
    if temperature:
        current_temperature = round(temperature - 273.15, 2)
        return {"Temperature of ":city.title(),"temp: ":{current_temperature}, "description: ":{description}, "IP is ": {client_host}, "time is ":{start_date}}
 
@app.get("/")
def home():
    a = 1
    return {"message": "The Weather-v1!", "??? no la cai gi day: ":a}
        
if __name__ == '__main__':
    uvicorn.run("main:app")
    