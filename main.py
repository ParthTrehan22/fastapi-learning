from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Server is live"}


# @app.get("/notes/{note_id}")
# def get_note(note_id: int):
#     return {"note_id": note_id}


@app.get("/notes/{attr}")
def get_note_desc(attr: str):
    if attr.isdigit():
        return {"desc": int(attr)}
    else: 
        return {"desc": attr}


@app.get("/notes/{note_id}/{desc}")
def get_note_info(note_id, desc):
    return {"message": f"The note at {note_id} is {desc}"}


@app.get("/list_notes")
def get_notes():
    return [{"note_id": 1, "message": "Note 1"}, {"note_id": 2, "message": "Note 2"}]


# def main():
#     print("Hello from fastapi-learning!")


# if __name__ == "__main__":
#     main()
