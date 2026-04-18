from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DnD Character Generator API is running!"}