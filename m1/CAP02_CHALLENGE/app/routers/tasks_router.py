"""
Módulo del Router de Tareas

Este router proporciona endpoints de API para gestionar tareas, incluyendo:
- Crear una nueva tarea
- Obtener una tarea específica por su ID
- Obtener todas las tareas
- Actualizar una tarea existente
- Eliminar una tarea específica
- Eliminar todas las tareas

El router utiliza inyección de dependencias para las sesiones de base de datos
y maneja varios métodos HTTP para las operaciones relacionadas con tareas.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Task, UpdateTaskModel, TaskList
from database import get_db, delete_all_tasks
from schemas import Message
from db import db

tasks_router = APIRouter()


@tasks_router.post("/", response_model=Task)
async def create_task(task: Task):
    """Crea una nueva tarea."""
    return db.add_task(task)


@tasks_router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Obtiene una tarea por su ID."""
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@tasks_router.get("/", response_model=TaskList)
async def get_tasks():
    """Obtiene la lista de todas las tareas."""
    tasks = db.get_tasks()
    return TaskList(tasks=tasks)


@tasks_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: UpdateTaskModel):
    """Actualiza una tarea existente por su ID."""
    updated_task = db.update_task(task_id, task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return updated_task


@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int):
    """Elimina una tarea específica por su ID."""
    db.delete_task(task_id)
    return {"message": "Tarea eliminada exitosamente"}


@tasks_router.delete("/all", response_model=Message, status_code=status.HTTP_200_OK)
def delete_all_tasks_endpoint(db_session: Session = Depends(get_db)):
    """Elimina todas las tareas de la base de datos."""
    try:
        deleted_count = delete_all_tasks(db_session)
        return {"message": f"Se eliminaron correctamente {deleted_count} tareas"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar todas las tareas: {str(e)}"
        )
