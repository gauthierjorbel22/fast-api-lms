from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel 

app = FastAPI(
    title='Fast API LMS', 
    description='LMS for managing students and courses', 
    version='0.01', 
    contact={
        'name':'Gauthier', 
        'email':'gauthierjorbel@gmail.com'
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]
    

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post('/users')
async def create_user(user:User):
    users.append(user)
    return {"message": "User created successfully"}

@app.get('/users/{id}')
async def get_user(id:int=Path(..., description="The ID of the user to get")):
    return users[id]