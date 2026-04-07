from fastapi import FastAPI,HTTPException
from sqlmodel import SQLModel
app = FastAPI()

class User(SQLModel):
    username: str
    password: str

db_users=[User(username="admin",password="admin"),
          User(username="user",password="admin"),
          User(username="guest",password="guest")]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
def login(user: User):
    for db_user in db_users:
        if db_user.username == user.username and db_user.password == user.password:
            return {"status": "success", "message": f"Bienvenido, {user.username}!"}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
