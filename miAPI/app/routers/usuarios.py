
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from app.models.usuario import UsuarioBase
from app.data.database import usuarios
from app.security.auth import verificar_Peticion

from sqlalchemy.orm import Session
from app.data.db import get_db
from app.data.usuario import Usuario

router= APIRouter(
    prefix="/v1/usuarios",
    tags=["CRUD Usuarios"]
)


@router.get("/")
async def leer_usuarios(db:Session=Depends(get_db)):
    
    consultausuarios= db.query(Usuario).all()
    return{
        "status":"200",
        "total": len(consultausuarios),
        "data":consultausuarios
    }
    
@router.get("/{id}")
async def leer_usuario_id(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrad")
    return {
        "status": "200",
        "data": usuario
    }

    
@router.post("/")
async def agregar_usuarios(usuario:UsuarioBase,db:Session=Depends(get_db)):
    
    nuevoUsuario=Usuario(nombre= usuario.nombre,edad= usuario.edad)
    
    db.add(nuevoUsuario)
    db.commit()
    db.refresh(nuevoUsuario)
    return{
        "mensaje":"Usuario agregado :D",
        "datos":nuevoUsuario,
        "status":"200"
    }
    
@router.put("/{id}")
async def actualizar_usuario(id: int, usuario_actualizado:UsuarioBase, db:Session=Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado :(")

    usuario.nombre = usuario_actualizado.nombre
    usuario.edad = usuario_actualizado.edad

    db.commit()
    db.refresh(usuario)
    return {
        "mensaje": "Usuario actualizado :)",
        "datos": usuario,
        "status": "200"
    }

@router.patch("/{id}")
async def actualizacion_parcial(id: int, datos: dict, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontradop :(")

    if "nombre" in datos:
        usuario.nombre = datos["nombre"]
    if "edad" in datos:
        usuario.edad = datos["edad"]

    db.commit()
    db.refresh(usuario)
    return {
        "mensaje": "Usuario actualizado parcialmente ;D",
        "datos": usuario,
        "status": "200"
    }

@router.delete("/{id}")
async def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()

    return {
        "mensaje": "Usuario eliminado",
        "status": "200"
    }