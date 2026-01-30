#importaciónes
from typing import Optional
from fastapi import FastAPI
import asyncio

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

@app.get("/v1/usuario/{id}", tags=['Parametro obligatorio'])
async def consultausuarios(id:int):
    await asyncio.sleep(4)
    return{"Usuario encontrado":"id"}

@app.get("/v1/usuarios_op/", tags=['Parametro opcional'])
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(4)
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id: 
                return {"usuario encontrado": id, "Datos": usuario}
        return {"mensaje": "Usuario no encontrado"}  
    else:
        return {"mensaje": "No se proporciono Id"}
 