from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select

app = FastAPI()
engine = create_engine("sqlite:///./database.db")

class usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

class Login(SQLModel):
    username: str
    password: str

@app.on_event("startup")
def inicio():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        if not s.exec(select(usuario).where(usuario.username == "admin")).first():
            s.add(usuario(username="admin", password="admin"))
            s.add(usuario(username="user", password="user"))
            s.add(usuario(username="guest", password="guest"))
            s.commit()

@app.post("/login")
def login(data: Login):
    with Session(engine) as s:
        user = s.exec(select(usuario).where(usuario.username == data.username)).first()
        if not user or user.password != data.password:
            raise HTTPException(401, "Usuario o contraseña incorrectos")
        return {"message": "Login exitoso", "username": user.username}