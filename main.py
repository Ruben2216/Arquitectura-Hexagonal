from fastapi import FastAPI, HTTPException
import json

from pweb2.users.application.services.user_servicio import UserServicio
from pweb2.users.infrastructure.persistence.datosMemoria import InMemoryUserRepository
from pweb2.users.domain.usuario import UserCreate, UserUpdate

from pweb2.pacientes.application.services.paciente_servicio import pacienteServicio
from pweb2.pacientes.infrastructure.persistence.datosMemoria import InMemoryPacienteRepository
from pweb2.pacientes.domain.paciente import pacienteCreate, pacienteUpdate

from pweb2.doctor.application.services.doctor_servicio import DoctorServicio
from pweb2.doctor.infrastructure.persistence.datosMemoria import InMemoryDoctorRepository
from pweb2.doctor.domain.doctor import DoctorCreate, DoctorUpdate

app = FastAPI()

# Inicializar repositorio en memoria y servicio
user_repository = InMemoryUserRepository()
user_service = UserServicio(user_repository)

paciente_repository = InMemoryPacienteRepository()
paciente_service = pacienteServicio(paciente_repository)

doctor_repository = InMemoryDoctorRepository()
doctor_service = DoctorServicio(doctor_repository)

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


#- Activar usuario
@app.patch("/users/{user_id}/activate")
def activate_user(user_id: str):
    user = user_service.activate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

#-----------------------------------
#END POINTS DE PACIENTES
#------------------------------------


# CREATE - Crear un nuevo paciente
@app.post("/pacientes", status_code=201)
def create_paciente(paciente_data: pacienteCreate):
    try:
        return paciente_service.registrar_paciente(paciente_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# READ - Obtener todos los pacientes
@app.get("/pacientes")
def get_all_pacientes():
    return paciente_service.get_all_paciente()


# READ - Obtener un paciente por ID
@app.get("/pacientes/{paciente_id}")
def get_paciente(paciente_id: str):
    paciente = paciente_service.get_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente


# UPDATE - Actualizar un paciente
@app.put("/pacientes/{paciente_id}")
def update_paciente(paciente_id: str, paciente_update: pacienteUpdate):
    try:
        paciente = paciente_service.update_paciente(paciente_id, paciente_update)
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return paciente
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE - Eliminar un paciente
@app.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: str):
    if not paciente_service.delete_paciente(paciente_id):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"message": "Paciente eliminado correctamente"}


# EXTRA - Desactivar paciente
@app.patch("/pacientes/{paciente_id}/deactivate")
def deactivate_paciente(paciente_id: str):
    paciente = paciente_service.deactivate_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente


#- Activar paciente
@app.patch("/pacientes/{paciente_id}/activate")
def activate_paciente(paciente_id: str):
    paciente = paciente_service.activate_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

#-----------------------
#END POINTS DE DOCTORES
#-----------------------

@app.post("/doctores", status_code=201)
def create_doctor(doctor_data: DoctorCreate):
    try:
        return doctor_service.registrar_doctor(doctor_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/doctores")
def get_all_doctores():
    return doctor_service.get_all_doctor()


@app.get("/doctores/{doctor_id}")
def get_doctor(doctor_id: str):
    doctor = doctor_service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor


@app.put("/doctores/{doctor_id}")
def update_doctor(doctor_id: str, doctor_update: DoctorUpdate):
    try:
        doctor = doctor_service.update_doctor(doctor_id, doctor_update)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")
        return doctor
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/doctores/{doctor_id}")
def delete_doctor(doctor_id: str):
    if not doctor_service.delete_doctor(doctor_id):
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return {"message": "Doctor eliminado correctamente"}
