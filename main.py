from uuid import UUID, uuid4
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from pydantic.fields import Field
from pydantic.tools import parse_obj_as
from sqlalchemy.sql.functions import user
from inputs_classes import MatrixInputs, UpdateMatrixInputs, UserDataOut
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
@app.post('/projects/{project_id}/{matrix_id}')
async def write_project_and_matrix(project_id: str, matrix_id: str, matrix: MatrixInputs):
    if matrix_id and project_id in matrices:
        return {
            "error": "Matrix already exists."
        }
    matrices[project_id, matrix_id] = matrix
    return matrices[project_id, matrix_id]

# GET PROJECT & MATRIX
@app.get('/projects/{project_id}/{matrix_id}')
async def read_matrix(project_id: str, matrix_id: str):
    return matrices[project_id, matrix_id]

# UPDATE PROJECT & MATRIX
@app.put('/projects/{project_id}/{matrix_id}')
async def updated_projects_and_matrix(project_id: str, matrix_id: str, matrix: UpdateMatrixInputs):
    if matrix.problem_statement and matrix.matrix_name != None:
        matrices[project_id, matrix_id] = matrix
    return matrices[project_id, matrix_id]