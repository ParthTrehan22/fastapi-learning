from fastapi import FastAPI
from pydantic import BaseModel

notes_db = []
next_id = 1

app = FastAPI()

class NoteCreate(BaseModel):
    title: str
    content: str
    pinned: bool = False

@app.post("/notes/create_note")
def create_note(note: NoteCreate):
    global next_id
    new_note = {"id": next_id, **note.model_dump()}
    notes_db.append(new_note)
    next_id += 1
    return new_note

@app.get("/notes")
def get_notes():
    return notes_db

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for n in notes_db:
        if n["id"] == note_id:
            return n        
    return {"error": "Note not found"}