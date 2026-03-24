
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

@router.delete("/{id}")
async def eliminar_usuario(id: int, usuarioAuth:str= Depends(verificar_Peticion)):
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