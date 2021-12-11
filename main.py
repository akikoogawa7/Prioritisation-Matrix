from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# create BaseModel Class for Matrix