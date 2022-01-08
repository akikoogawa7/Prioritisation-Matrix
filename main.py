from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql.functions import user
from sqlalchemy.orm import Session
from schemas import Matrix
from db import get_db
from models import MatrixORM
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

db = []

hostname = socket.gethostname()
version = f"{sys.version_info.major}.{sys.version_info.minor}"

# @app.post('/')
# def create(details: Matrix, db: Session()):
#     new_matrix = Matrix(
#         name = details.name,
#         description = details.description,
#         problem_statement = details.problem_statement,
#     )
#     db.add()
#     db.commit()
#     db.close()

# @app.post('/')
# def create(details: Matrix, db: Session = Depends(get_db)):
#     to_create = Matrix(
#         name = details.name,
#         description = details.description,
#         problem_statement = details.problem_statement,
#     )
#     db.add(to_create)
#     db.commit()
#     return {
#         "success": True,
#         "created_id": to_create.id
#     }

# @app.get('/')
# def get_by_id(id: int, db: Session = Depends(get_db)):
#     return db.query(Matrix).filter(Matrix.id == id).first()

# POST USER
# @app.post('/users/{user_id}')
# async def write_user(user_id: str, user_data: UserDataOut):
#     if user_id in matrices:
#         return {
#             "error": "User already exists."
#         }
#     matrices[user_id] = user_data
#     return matrices[user_id]

# GET USERS
# @app.get('/users')
# def read_user():
#     return db

# GET USERS BY ID
# @app.get('/users/{user_id}')
# async def read_user(user_id: str = Path(None, description='Please add user id')):
#     return matrices[user_id]

# GET MATRIX
@app.get('/matrices')
def get_matrices():
    return db

# GET MATRIX BY ID
@app.get('/matrices/{matrix_id}')
def get_matrix_by_id(matrix_id: int):
    return db[matrix_id-1]

# POST MATRIX
@app.post('/matrices')
def create_matrix(matrix: Matrix):
    db.append(matrix.dict())
    return db[-1]

# DELETE MATRIX
@app.delete('/matrices/{matrix_id}')
def delete_matrix(matrix_id: int):
    db.pop(matrix_id-1)
    return {}

# # UPDATE MATRIX
# @app.put('matrices')
# def update_matrix(matrix: Matrix)

# POST PROJECT & MATRIX
# @app.post('/projects/{project_id}/{matrix_id}')
# async def write_project_and_matrix(project_id: str, matrix_id: str, matrix: MatrixInputs):
#     if matrix_id and project_id in matrices:
#         return {
#             "error": "Matrix already exists."
#         }
#     matrices[project_id, matrix_id] = matrix
#     return matrices[project_id, matrix_id]

# # GET PROJECT & MATRIX
# @app.get('/projects/{project_id}/{matrix_id}')
# async def read_matrix(project_id: str, matrix_id: str):
#     return matrices[project_id, matrix_id]

# # UPDATE PROJECT & MATRIX
# @app.put('/projects/{project_id}/{matrix_id}')
# async def updated_projects_and_matrix(project_id: str, matrix_id: str, matrix: UpdateMatrixInputs):
#     if matrix.problem_statement and matrix.matrix_name != None:
#         matrices[project_id, matrix_id] = matrix
#     return matrices[project_id, matrix_id]