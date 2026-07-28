from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import Field

notes_db = []
next_id = 1

app = FastAPI()

class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    pinnned: bool = False


class NoteOut(BaseModel):
    id: int
    title: str
    content: str


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


@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    for n in notes_db:
        if n["id"] == note_id:
            return n
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/edit/{note_id}", response_model=NoteOut)
def edit_note(note_id: int, note: NoteCreate):
    for n in notes_db:
        if n["id"] == note_id:
            n.update(note.model_dump())
            return n
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/delete/{note_id}")
def delete_note(note_id: int):
    for i, n in enumerate(notes_db):
        if n["id"] == note_id:
            notes_db.pop(i)
            return {"deleted": note_id}
    raise HTTPException(status_code=404, detail="Note not found")
