from fastapi import FastAPI, HTTPException
import json

from pweb2.users.application.services.user_servicio import UserServicio
from pweb2.users.infrastructure.persistence.datosMemoria import InMemoryUserRepository
from pweb2.users.domain.usuario import UserCreate, UserUpdate

app = FastAPI()

# Inicializar repositorio en memoria y servicio
user_repository = InMemoryUserRepository()
user_service = UserServicio(user_repository)

with open('recetas.json', 'r', encoding='utf-8') as archivo:
    datosRecetas = json.load(archivo)


@app.get("/")
def read_root():
    return {"Hola": "World"}

#Buscar receta por ID

@app.get("/recetas/{recetaId}")
def read_receta( recetaId:int):
    for receta in datosRecetas["receta"]:
        if receta["id"] == recetaId:
            return receta


# CREATE - Crear un nuevo usuario
@app.post("/users", status_code=201)
def create_user(user_data: UserCreate):
    try:
        return user_service.registrar_User(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# READ - Obtener todos los usuarios
@app.get("/users")
def get_all_users():
    return user_service.get_all_user()


# READ - Obtener un usuario por ID
@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


# UPDATE - Actualizar un usuario
@app.put("/users/{user_id}")
def update_user(user_id: str, user_update: UserUpdate):
    try:
        user = user_service.update_user(user_id, user_update)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE - Eliminar un usuario
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado correctamente"}


# EXTRA - Desactivar usuario
@app.patch("/users/{user_id}/deactivate")
def deactivate_user(user_id: str):
    user = user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


# EXTRA - Activar usuario
@app.patch("/users/{user_id}/activate")
def activate_user(user_id: str):
    user = user_service.activate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


