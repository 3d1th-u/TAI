#importaciónes
from typing import Optional
from fastapi import FastAPI, status, HTTPException
import asyncio
from pydantic import BaseModel, Field

#inicialización
app= FastAPI(
    title= 'mi primer API',
    description= 'Edith :)',
    version= '1.0'
)

usuarios=[
    {"id":1, "nombre":"Chabela", "edad":20},
    {"id":2, "nombre":"Raquel", "edad":44},
    {"id":3, "nombre":"Juana", "edad":33},
]

#modelo de validacion pydantic
class UsuarioBase(BaseModel):
    id:int = Field(...,gt=0, description="Identificador de usuario", example="1")
    nombre:str = Field(...,min_length=3, max_length=50, description="Nombre del usuario")
    edad:int = Field(...,ge=0, le=121, description="Edad validad entre 0 y 121")


#endpoints
@app.get("/", tags=['Inicio'])
async def holamundo():
    return{"mensaje":"holamundo FASTAPI"}

@app.get("/bienvenidos", tags=['Inicio'])
async def bienvenidos():
    return{"mensaje":"Bienvenidos FASTAPI"}

@app.get("/v1/calificaciones", tags=['Asincronia'])
async def calificaciones():
    await asyncio.sleep(5)
    return{"mensaje":"Tu calificacion en TAI es 10"}

@app.get("/v1/parametroO/{id}", tags=['Parametro obligatorio'])
async def consultausuarios(id:int):
    await asyncio.sleep(4)
    return{"Usuario encontrado":"id"}


@app.get("/v1/parametroOp/", tags=['Parametro opcional'])
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(4)
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id: 
                return {"usuario encontrado": id, "Datos": usuario}
        return {"mensaje": "Usuario no encontrado"}  
    else:
        return {"mensaje": "No se proporciono Id"}
 
@app.get("/v1/usuarios/", tags=['CRUD Usuarios'])
async def consultausuarios():
    return{
        "status":"200",
        "total": len(usuarios),
        "data":usuarios
    }
    
@app.post("/v1/usuarios/", tags=['CRUD Usuarios'])
async def agregar_usuarios(usuario:UsuarioBase):
    for usr in usuarios:
        if usr["id"]== usuario.id:
            raise HTTPException(
                status_code=400,
                detail="El ID ya existe"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"Usuario agregado :D",
        "datos":usuario,
        "status":"200"
    }
    
@app.put("/v1/usuarios/{id}", tags=['CRUD Usuarios'])
async def actualizar_usuario(id: int, usuario_actualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado
            return {
                "mensaje": "Usuario actualizado :)",
                "datos": usuario_actualizado,
                "status": "200"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

@app.delete("/v1/usuarios/{id}", tags=['CRUD Usuarios'])
async def eliminar_usuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {
                "mensaje": "Usuario eliminado",
                "datos": usr,
                "status": "200"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
        
        