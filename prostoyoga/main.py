from typing import List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .models import Training, User

app = FastAPI(
    title="ProstoYoga"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Olga"},
    {"id": 2, "role": "coach", "name": "Sveta"},
    {"id": 3, "role": "user", "name": "Yury"}
]

fake_training = [
    {'id': 1, 'day': 30, 'month': 10, 'year': 2022, 'time': 6423462346},
    {'id': 2, 'day': 15, 'month': 10, 'year': 2022, 'time': 3623634523},
]


@app.get("/")
def root():
    return HTMLResponse(content="Hello")


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.post("/users")
def add_user():
    pass


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


@app.get('/training/{training_id}', response_model=List[Training])
def get_training(training_id: int):
    return list(filter(lambda training: training.get('id') == training_id, fake_training))


@app.post('/training')
def add_training(training_list: List[Training]):
    fake_training.extend(training_list)
    return {"status": 200, "data": fake_training}


@app.delete('/training')
def delete_training(training_list: List[Training]):
    pass


@app.put('/training')
def change_training(training_list: List[Training]):
    pass
