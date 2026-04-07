# Login API con FastAPI

## Instalación
pip install -r requirements.txt

## Ejecución
uvicorn main:app --reload

## Ejemplos

### Login exitoso
curl -X POST "http://127.0.0.1:8000/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "admin"}'

# Respuesta:
# {"status":"success","message":"Bienvenido, admin!"}

### Login fallido
curl -X POST "http://127.0.0.1:8000/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "wrong"}'

# Respuesta:
# {"detail":"Usuario o contraseña incorrectos"}

## Documentación interactiva
http://127.0.0.1:8000/docs
