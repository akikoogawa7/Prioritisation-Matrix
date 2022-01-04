from uuid import UUID, uuid4
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from pydantic.fields import Field
from pydantic.tools import parse_obj_as
from sqlalchemy.sql.functions import user
from inputs_classes import UserData, MatrixInputs, UserElementInputs, UserDataOut
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
    'project_title': 'Title',
    'matrix_name': 'matrix1',
    'user_id': 'akiko12',
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
    matrices[user_id] = {'user_id': user_id,'username': user_data.username}
    return matrices[user_id]

# GET USER
@app.get('/users/{user_id}')
async def read_user(user_id: str = Path(None, description='Please add user id')):
    return matrices[user_id]
 
# GET PROJECT & MATRIX
@app.get('/projects/{project_title}/{matrix_name}')
async def read_matrix(*, project_title: str, project_description: Optional[str] = None, matrix_name: str):
    return {
        'project_title': project_title,
        'project_description': project_description,
        'matrix_name': matrix_name,
    }

# GET MATRIX BY MATRIX ID 
@app.get('/matrix/{matrix_id}')
async def read_matrix(matrix: MatrixInputs, author: UserDataOut, matrix_id: int = Path(None, description="The ID of your matrix")):
    if matrix_id in matrices:
        return {
            "error": "Matrix already exists"
        }
    matrices[matrix_id] = {'matrix_id': matrix.id}
    return matrices[matrix_id]
