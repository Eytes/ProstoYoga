import os
from os.path import join, dirname

from dotenv import load_dotenv
from fastapi import FastAPI


app = FastAPI()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DATABASE_URL = os.getenv("DATABASE_URL")
