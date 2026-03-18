
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from app.models.usuario import UsuarioBase
from app.data.database import usuarios
from app.security.auth import verificar_Peticion

router= APIRouter(
    prefix="/v1/usuarios",
    tags=["CRUD Usuarios"]
)


@router.get("/")
async def consultausuarios():
    return{
        "status":"200",
        "total": len(usuarios),
        "data":usuarios
    }

    
@router.post("/")
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