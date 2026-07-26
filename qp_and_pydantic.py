from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class NoteCreate(BaseModel):
    title: str
    content: str
    pinned: bool = False
    
@app.post('/notes/create')
def create_note(note: NoteCreate):
    return {"recieved": note}