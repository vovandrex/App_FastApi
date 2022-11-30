from typing import Optional, List
from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from api import users,sections,courses

app = FastAPI(
    title="AppFastApi",
    description="My first web app",
    version="0.0.1",
    contact={"name": "Vladimir"}
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)







