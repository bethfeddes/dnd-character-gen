from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    password: str

class CharacterBase(BaseModel):
    name: str
    char_level: int
    char_class: str
    char_species: str
    char_background: str

@app.get("/")
def root():
    return {"message": "DnD Character Generator API is running!"}