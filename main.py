from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DnD Character Generator API is running!"}