from uuid import UUID, uuid4
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from pydantic.fields import Field
from pydantic.tools import parse_obj_as
from sqlalchemy.sql.functions import user
from inputs_classes import MatrixInputs, UserDataOut
import socket
import sys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

matrices = {
}

hostname = socket.gethostname()
version = f"{sys.version_info.major}.{sys.version_info.minor}"

@app.get('/')
async def read_root():
    return {
        "name": "hivesquared",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
    }

# POST USER
@app.post('/users/{user_id}')
async def write_user(user_id: str, user_data: UserDataOut):
    if user_id in matrices:
        return {
            "error": "User already exists."
        }
    matrices[user_id] = user_data
    return matrices[user_id]

# GET USER
@app.get('/users/{user_id}')
async def read_user(user_id: str = Path(None, description='Please add user id')):
    return matrices[user_id]

# POST PROJECT & MATRIX
@app.post('/projects/{project_name}/{matrix_name}')
async def write_project_and_matrix(project_name: str, matrix_name: str, matrix: MatrixInputs):
    if matrix_name and project_name in matrices:
        return {
            "error": "Matrix already exists."
        }
    matrices[project_name, matrix_name] = matrix
    return matrices[project_name, matrix_name]
 
# GET PROJECT & MATRIX
@app.get('/projects/{project_title}/{matrix_name}')
async def read_matrix(project_title: str, matrix_name: str):
    return matrices[project_title, matrix_name]
        
# POST MATRIX
@app.post('/matrix/{matrix_name}')
async def write_matrix(matrix_name: str, matrix: MatrixInputs):
    if matrix_name in matrices:
        return {
            "error": "Matrix already exists"
        }
    matrices[matrix_name] = matrix
    return matrices[matrix_name]

# POST PROJECT
@app.post('/projects/{project_title}')
async def write_project(project_title: str, matrix: MatrixInputs):
    if project_title in matrices:
        return {
            "error": "Matrix already exists"
        }
    matrices[project_title] = matrix
    return matrices[project_title]

# GET MATRIX
@app.get('/matrix/{matrix_name}')
async def read_matrix_name(matrix_name: str = Path(None, description="The name of your matrix")):
    return matrices[matrix_name]

# GET PROJECTS 
@app.get('/projects/{project_title}')
async def read_project_title(project_title: str = Path(None, description="The title of your project")):
    return matrices[project_title]
