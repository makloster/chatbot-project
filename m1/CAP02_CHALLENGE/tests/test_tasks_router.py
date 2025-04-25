"""
Pruebas unitarias para el router de tareas.
Este módulo contiene pruebas para verificar la funcionalidad y validaciones
implementadas en el router de tareas.
"""

import pytest
from fastapi.testclient import TestClient
from fastapi import status
from unittest.mock import patch, MagicMock

from main import app
from models import Task, UpdateTaskModel
from db import db

client = TestClient(app)


@pytest.fixture
def mock_db():
    """Fixture para mockear la base de datos durante las pruebas."""
    with patch('db.db') as mock:
        yield mock


@pytest.fixture
def sample_task():
    """Fixture que proporciona una tarea de ejemplo."""
    return Task(id=1, title="Test Task", description="Test Description", completed=False)


class TestCreateTask:
    """Pruebas para el endpoint de creación de tareas."""

    def test_create_task_success(self, mock_db, sample_task):
        """Prueba la creación exitosa de una tarea."""
        mock_db.add_task.return_value = sample_task

        response = client.post(
            "/tasks/",
            json={"id": 1, "title": "Test Task", "description": "Test Description", "completed": False}
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": False
        }
        mock_db.add_task.assert_called_once()

    def test_create_task_empty_title(self, mock_db):
        """Prueba que no se puede crear una tarea con título vacío."""
        response = client.post(
            "/tasks/",
            json={"id": 1, "title": "", "description": "Test Description", "completed": False}
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "título de la tarea no puede estar vacío" in response.json()["detail"]
        mock_db.add_task.assert_not_called()

    def test_create_completed_task_without_description(self, mock_db):
        """Prueba que no se puede crear una tarea completada sin descripción."""
        response = client.post(
            "/tasks/",
            json={"id": 1, "title": "Test Task", "description": "", "completed": True}
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "tareas completadas deben tener una descripción" in response.json()["detail"]
        mock_db.add_task.assert_not_called()


class TestGetTask:
    """Pruebas para el endpoint de obtención de tareas."""

    def test_get_task_success(self, mock_db, sample_task):
        """Prueba la obtención exitosa de una tarea por ID."""
        mock_db.get_task.return_value = sample_task

        response = client.get("/tasks/1")

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": False
        }
        mock_db.get_task.assert_called_once_with(1)

    def test_get_task_not_found(self, mock_db):
        """Prueba que se devuelve un error 404 cuando la tarea no existe."""
        mock_db.get_task.return_value = None

        response = client.get("/tasks/999")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "no encontrada" in response.json()["detail"]
        mock_db.get_task.assert_called_once_with(999)

    def test_get_task_invalid_id(self):
        """Prueba que se valida correctamente el ID de la tarea."""
        response = client.get("/tasks/0")

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestGetTasks:
    """Pruebas para el endpoint de obtención de todas las tareas."""

    def test_get_all_tasks(self, mock_db):
        """Prueba la obtención de todas las tareas."""
        mock_db.get_tasks.return_value = [
            Task(id=1, title="Task 1", description="Description 1", completed=False),
            Task(id=2, title="Task 2", description="Description 2", completed=True)
        ]

        response = client.get("/tasks/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()["tasks"]) == 2
        mock_db.get_tasks.assert_called_once()

    def test_get_tasks_with_completed_filter(self, mock_db):
        """Prueba el filtrado de tareas por estado de completado."""
        mock_db.get_tasks.return_value = [
            Task(id=1, title="Task 1", description="Description 1", completed=False),
            Task(id=2, title="Task 2", description="Description 2", completed=True)
        ]

        response = client.get("/tasks/?completed=true")

        assert response.status_code == status.HTTP_200_OK
        tasks = response.json()["tasks"]
        assert len(tasks) == 1
        assert tasks[0]["id"] == 2
        assert tasks[0]["completed"] is True

    def test_get_tasks_with_limit(self, mock_db):
        """Prueba la limitación del número de tareas devueltas."""
        mock_db.get_tasks.return_value = [
            Task(id=i, title=f"Task {i}", description=f"Description {i}", completed=False)
            for i in range(1, 6)
        ]

        response = client.get("/tasks/?limit=3")

        assert response.status_code == status.HTTP_200_OK
        tasks = response.json()["tasks"]
        assert len(tasks) == 3


class TestUpdateTask:
    """Pruebas para el endpoint de actualización de tareas."""

    def test_update_task_success(self, mock_db, sample_task):
        """Prueba la actualización exitosa de una tarea."""
        mock_db.get_task.return_value = sample_task
        updated_task = Task(id=1, title="Updated Task", description="Updated Description", completed=True)
        mock_db.update_task.return_value = updated_task

        response = client.put(
            "/tasks/1",
            json={"title": "Updated Task", "description": "Updated Description", "completed": True}
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": 1,
            "title": "Updated Task",
            "description": "Updated Description",
            "completed": True
        }
        mock_db.update_task.assert_called_once()

    def test_update_task_not_found(self, mock_db):
        """Prueba que se devuelve un error 404 cuando la tarea a actualizar no existe."""
        mock_db.get_task.return_value = None

        response = client.put(
            "/tasks/999",
            json={"title": "Updated Task"}
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_db.update_task.assert_not_called()

    def test_update_task_empty_title(self, mock_db, sample_task):
        """Prueba que no se puede actualizar una tarea con título vacío."""
        mock_db.get_task.return_value = sample_task

        response = client.put(
            "/tasks/1",
            json={"title": ""}
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "título de la tarea no puede estar vacío" in response.json()["detail"]
        mock_db.update_task.assert_not_called()

    def test_update_task_completed_without_description(self, mock_db, sample_task):
        """Prueba que no se puede marcar como completada una tarea sin descripción."""
        sample_task.description = ""
        mock_db.get_task.return_value = sample_task

        response = client.put(
            "/tasks/1",
            json={"completed": True}
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "tareas completadas deben tener una descripción" in response.json()["detail"]
        mock_db.update_task.assert_not_called()


class TestDeleteTask:
    """Pruebas para el endpoint de eliminación de tareas."""

    def test_delete_task_success(self, mock_db, sample_task):
        """Prueba la eliminación exitosa de una tarea."""
        mock_db.get_task.return_value = sample_task

        response = client.delete("/tasks/1")

        assert response.status_code == status.HTTP_200_OK
        assert "eliminada exitosamente" in response.json()["message"]
        mock_db.delete_task.assert_called_once_with(1)

    def test_delete_task_not_found(self, mock_db):
        """Prueba que se devuelve un error 404 cuando la tarea a eliminar no existe."""
        mock_db.get_task.return_value = None

        response = client.delete("/tasks/999")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        mock_db.delete_task.assert_not_called()


class TestDeleteAllTasks:
    """Pruebas para el endpoint de eliminación de todas las tareas."""

    @patch('database.delete_all_tasks')
    def test_delete_all_tasks_success(self, mock_delete_all, mock_db):
        """Prueba la eliminación exitosa de todas las tareas."""
        mock_delete_all.return_value = 5

        response = client.delete("/tasks/all?confirm=true")

        assert response.status_code == status.HTTP_200_OK
        assert "Se eliminaron correctamente 5 tareas" in response.json()["message"]
        mock_delete_all.assert_called_once()

    @patch('database.delete_all_tasks')
    def test_delete_all_tasks_without_confirmation(self, mock_delete_all, mock_db):
        """Prueba que se requiere confirmación para eliminar todas las tareas."""
        response = client.delete("/tasks/all?confirm=false")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "Se requiere confirmación" in response.json()["detail"]
        mock_delete_all.assert_not_called()

    @patch('database.delete_all_tasks')
    def test_delete_all_tasks_no_tasks(self, mock_delete_all, mock_db):
        """Prueba el caso donde no hay tareas para eliminar."""
        mock_delete_all.return_value = 0

        response = client.delete("/tasks/all?confirm=true")

        assert response.status_code == status.HTTP_200_OK
        assert "No hay tareas para eliminar" in response.json()["message"]
        mock_delete_all.assert_called_once()

    @patch('database.delete_all_tasks')
    def test_delete_all_tasks_error(self, mock_delete_all, mock_db):
        """Prueba el manejo de errores al eliminar todas las tareas."""
        mock_delete_all.side_effect = Exception("Database error")

        response = client.delete("/tasks/all?confirm=true")

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "Error al eliminar todas las tareas" in response.json()["detail"]
        mock_delete_all.assert_called_once()
