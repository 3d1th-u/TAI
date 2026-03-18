#importaciónes
from fastapi import FastAPI
from app.routers import usuarios, misc


#inicialización
app= FastAPI(
    title= 'mi primer API',
    description= 'Edith :)',
    version= '1.0'
)

app.include_router(usuarios.router)

app.include_router(misc.router)    

           