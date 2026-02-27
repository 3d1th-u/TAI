#importaciónes
from fastapi import FastAPI, status, HTTPException
import asyncio
from pydantic import BaseModel, Field

#inicialización
app= FastAPI(
    title= 'Biblioteca',
    description= 'API de biblioteca',
    version= '1.0'
)

#simulación de BD
libros = []
prestamos = []

#modelo de validacion pydantic del libro
class Libro(BaseModel):
    id: int
    nombre: str = Field(min_length=2, max_length=100)
    autor: str
    año: int = Field(gt=1450, le=2026)
    paginas: int = Field(gt=1)
    estado: str = "disponible"
    
#modelo de validacion pydantic del libro
class Usuario(BaseModel):
    nombre: str
    correo: str
    
# modelo de validacion del prestamo
class Prestamo(BaseModel):
    id: int
    libro_id: int
    usuario: Usuario



#endpoints
@app.get("/", tags=['Inicio'])
async def holaAPIbiblioteca():
    return{"mensaje":"hola biblioteca digital :b"}

#mostrar libros
@app.get("/v1/libros/")
async def listar_libros():
    return {
        "total": len(libros),
        "data": libros
    }

#regsitrar libros
@app.post("/v1/libros/", status_code=201)
async def registrar_libro(libro: Libro):
    for l in libros:
        if l["id"] == libro.id:
            raise HTTPException(status_code=400, detail="El libro ya existe ;D")
    libros.append(libro.dict())
    return {
        "mensaje": "Libro registrado correctamente",
        "status": "201"
    }

# registrar un prestamo
@app.post("/v1/prestamos/", status_code=201)
async def prestar_libro(prestamo: Prestamo):
    for l in libros:
        if l["id"] == prestamo.libro_id:
            if l["estado"] == "prestado":
                raise HTTPException(status_code=409, detail="Libro ya prestado")
            l["estado"] = "prestado"
            prestamos.append(prestamo.dict())
            return {
                "mensaje": "Prestamo registrado"
            }
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# devolución
@app.put("/v1/prestamos/devolver/{id}")
async def devolver_libro(id: int):
    for p in prestamos:
        if p["id"] == id:
            for l in libros:
                if l["id"] == p["libro_id"]:
                    l["estado"] = "disponible"
            prestamos.remove(p)
            return {
                "mensaje": "Libro devuelto"
            }
    raise HTTPException(status_code=409, detail="Prestamo no existe")

# buscar libro por nombre
@app.get("/v1/libros/buscar/{nombre}")
async def buscar_libro(nombre: str):
    for l in libros:
        if l["nombre"].lower() == nombre.lower():
            return l
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# eliminar registro de prestamo
@app.delete("/v1/prestamos/{id}")
async def eliminar_prestamo(id: int):
    for p in prestamos:
        if p["id"] == id:
            prestamos.remove(p)
            return {
                "mensaje": "Prestamo eliminado"
            }
    raise HTTPException(status_code=409, detail="Prestamo no existe")
        
        