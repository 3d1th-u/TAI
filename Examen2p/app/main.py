#IMPORTACIONES
from typing import Optional
from fastapi import FastAPI, status, HTTPException, Depends
import asyncio
from pydantic import BaseModel, Field
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets


app= FastAPI()


#BASE DE DATOS FICTICIA
citas=[
    {"id":1, "nombre":"Chabela", "motivo":"esguince" },
    {"id":2, "nombre":"Raquel", "motivo":"fiebre"},
    {"id":3, "nombre":"Juana", "motivo":"tos seca"},
]


#MODELO DE VALIDACIÓN DE DATOS
class CitaBase(BaseModel):
    id:int = Field(..., gt=0),
    nombre:str = Field(...,min_length=5, max_length=50),
    #fecha:
    motivo:str = Field(...,min_length=5, max_length=100),
    #confirmacion:bool = Field(...,),
    #citas:

#SEGURIDAD
security= HTTPBasic()
def verificar_peticion(credentials: HTTPBasicCredentials=Depends(security)):
    usuarioAuth=secrets.compare_digest(credentials.username,"root")
    contraAuth=secrets.compare_digest(credentials.password,"1234")
    
    if not(usuarioAuth and contraAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Las credenciales no son validas"
        )
    return credentials.username


#ENDPOITS 
@app.get("/")
async def ssijala():
    return{"mensaje":"si jaló"}
    
#ENDPOINT CREAR CITA
@app.post("/v1/crearCita/", tags=['CRUD CIATS'])
async def crear_cita(cita:CitaBase):
    for cit in citas:
        if cit["id"]== citas.id:
            raise HTTPException(
                status_code=400,
                detail= "Este ID ya existe"
            )
        citas.append(citas)
        return{
            "mensaje":"La cita fue agregada :p",
            "datos": citas,
            "status":"200"
        }
        
#ENDPOINT LISTAR CITA
@app.get("/v1/citas/",  tags=['CRUD CITAS'])
async def consultar_cita(cita:CitaBase, usuarioAuth:str=Depends(verificar_peticion)):
    return{
        "status":"200",
        "total":len(citas),
        "data":citas
    }

#ENDPOINT CONSULTAR POR ID
@app.get("/v1/citasconsul/{id}", tags=['CRUD CITAS'])
async def consultar_cita(cita:CitaBase):
    return{
        "status":"200",
        "total":len(citas),
        "data":citas
    }

#ENDPOINT CONFIRMAR CITA
#ENDPOINT ELIMINAR CITA
@app.delete("/v1/citas/{id}", tags='CRUD CITAS')
async def eliminar_cita(id: int, usuarioAuth:str=Depends(verificar_peticion)):
    for cit in citas:
        if cit["id"] == id:
            citas.remove(cit)
            return{
                "mensaje":"Cita eliminada",
                "datos":cit,
                "status":"200"
            }
    raise HTTPException(
        status_code=404,
        detail="Cita no encontrada"
    )

