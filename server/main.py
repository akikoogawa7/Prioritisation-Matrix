from uuid import UUID, uuid4
from fastapi import FastAPI, Path
from typing import List, Optional
from .inputs_classes import UserData, MatrixInputs, UserElementInputs, UserDataOut
import socket
import sys

app = FastAPI()


matrices = {
    'matrix_body': {
        'matrix_id': 1,
        'problem_statement': 'How to solve this'
    }
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

@app.post('/user/', response_model=UserDataOut)
async def create_user(user: UserData):
    return user

@app.get('/matrices/')
async def get_matrices(matrix_name: str, matrix_body: MatrixInputs):
    return {'matrix_name': matrix_name, 'matrix_body': matrix_body}

@app.put('/{project_title}/matrices/{matrix_name}/{problem_statement}')
async def read_item_public_data(project_title: str, matrix_name: str, problem_statement: str, matrix: MatrixInputs, project_description: Optional[str] = None):
    return {'project_title': project_title, 
    'project_description': project_description, 
    'matrix_name': matrix_name, 
    'problem_statement': problem_statement,
    'matrix': matrix 
    }

@app.post('/elements/{element_name}')
async def create_element(element_name: str, element_body: UserElementInputs, element_list: List[UserElementInputs]):
    element_list.append({'element_name': element_name, 'element_body': element_body})
    return {'element_name': element_name, 'element_body': element_body, 'element_list': element_list}

@app.get('matrices/{matrix_id}.')
async def get_matrix(name: str, matrix_id: int = Path(None, description='The ID of the matrix you would like to view') ):
    for matrix in matrices:
        if matrices[matrix_id]['problem_statement'] == name:
            return matrices['problem_statement']




