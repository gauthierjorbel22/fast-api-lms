from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel 
from api import users, courses, sections



app = FastAPI(
    title='Fast API LMS', 
    description='LMS for managing students and courses', 
    version='0.01', 
    contact={
        'name':'Gauthier', 
        'email':'gauthierjorbel@gmail.com'
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)