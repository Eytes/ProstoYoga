import os
from os.path import join, dirname

from dotenv import load_dotenv


_dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(_dotenv_path)
DATABASE_URL = os.getenv("DATABASE_URL")
