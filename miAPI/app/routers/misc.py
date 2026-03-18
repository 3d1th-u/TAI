
from fastapi import APIRouter
import asyncio
from typing import Optional
from app.data.database import usuarios

router= APIRouter(tags=["Varios"])


#endpoints
@router.get("/")
async def holamundo():
    return{"mensaje":"holamundo FASTAPI"}

@router.get("/bienvenidos")
async def bienvenidos():
    return{"mensaje":"Bienvenidos FASTAPI"}

@router.get("/v1/calificaciones")
async def calificaciones():
    await asyncio.sleep(5)
    return{"mensaje":"Tu calificacion en TAI es 10"}

@router.get("/v1/parametroO/{id}")
async def consultausuarios(id:int):
    await asyncio.sleep(4)
    return{"Usuario encontrado":"id"}


@router.get("/v1/parametroOp/")
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(4)
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id: 
                return {"usuario encontrado": id, "Datos": usuario}
        return {"mensaje": "Usuario no encontrado"}  
    else:
        return {"mensaje": "No se proporciono Id"}
 

        
  