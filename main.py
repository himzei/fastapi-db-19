from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from pydantic import BaseModel

DATABASE_URL = 


app = FastAPI()

@app.get("/")
def read_home():
    return {
        "hello" : "world"
    }