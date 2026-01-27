#importaciónes
from fastapi import FastAPI

#inicialización
app= FastAPI()

#endpoints
@app.get("/")
async def holamundo():
    return{"mensaje":"holamundo FASTAPI"}

@app.get("/bienvenidos")
async def bienvenidos():
    return{"mensaje":"Bienvenidos FASTAPI"}