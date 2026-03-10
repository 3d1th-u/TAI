#IMPORTACIONES
from typing import Optional
from fastapi import FastAPI, status, HTTPException, Depends
import asyncio
from pydantic import BaseModel, Field
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

#BASE DE DATOS FICTICIA


#MODELO DE VALIDACIÓN DE DATOS
class CitaBase(BaseModel):
    id:int = Field(..., gt=0),
    nombre:str = Field(...,min_length=5, max_length=50),
    #fecha:
    motivo:str = Field(...,min_length=5, max_length=100),
    confirmacion:bool = Field(...,),
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
#ENDPOINT CREAR CITA
@app.post("/v1/crearCita")
async def crear_cita(usuario:UsuarioBase):
    for usu in usuarios:
        if usu["id"]== usuario.id:
            raise HTTPException(
                status_code=400,
                detail= "Este ID ya existe"
            )
        usuarios.append(usuario)
        return{
            "mensaje":"El usuario fue agregado :p"
            "datos":usuario,
            "status":"200"
        }
        
#ENDPOINT LISTAR CITA

#ENDPOINT CONSULTAR POR ID

#ENDPOINT CONFIRMAR CITA

#ENDPOINT ELIMINAR CITA

