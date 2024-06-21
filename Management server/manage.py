from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid
from database import database, submissions

app = FastAPI()

# Define the submission model
class Submission(BaseModel):
    username: str
    password: str
    code: str

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/submission")
async def create_submission(submission: Submission):
    query = submissions.insert().values(
        id=str(uuid.uuid4()),
        username=submission.username,
        password=submission.password,
        code=submission.code,
        status="SUBMITTED",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    record_id = await database.execute(query)
    return {"id": record_id}

@app.patch("/submission")
async def update_submission(id: str, status: str):
    query = submissions.update().where(submissions.c.id == id).values(
        status=status,
        updated_at=datetime.now()
    )
    await database.execute(query)
    return {"status": "updated"}

@app.get("/submission")
async def get_submission(username: str, password: str, id: str):
    query = submissions.select().where(
        submissions.c.username == username,
        submissions.c.password == password,
        submissions.c.id == id
    )
    submission = await database.fetch_one(query)
    if submission:
        return submission
    else:
        raise HTTPException(status_code=404, detail="Submission not found")

