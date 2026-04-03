# API de Login con FastAPI

API de autenticación usando FastAPI y SQLModel con base de datos local embebida en código.

## Requisitos
- Python 3.10+

## Instalación
pip install -r requirements.txt

## Ejecución
uvicorn main:app --reload

La API estará disponible en: http://127.0.0.1:8000  
Documentación interactiva en: http://127.0.0.1:8000/docs

## Endpoint

### POST /iniciar-sesion

**Body:**
{
  "nombre_usuario": "admin",
  "contrasena": "admin"
}

**Respuesta exitosa (200):**
{
  "mensaje": "Inicio de sesión exitoso",
  "usuario": "admin"
}

**Respuesta fallida (401):**
{
  "detail": "Usuario o contraseña incorrectos"
}

## Usuarios de prueba
usuarios: admin,user,guest 
## Contraseñas de prueba
contraseñas: admin,user,guest
