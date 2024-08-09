from ninja import Router
from typing import List
from utils import ServiceUnavailableError

from django.shortcuts import get_object_or_404

from ..models import Task
from .entity import TaskRequestEntity, TaskResponseEntity


router = Router()


@router.get("/list", response=List[TaskResponseEntity])
def list_all_tasks(request):
    task_list = Task.objects.all()
    return task_list

@router.get("/{task_id}", response=TaskResponseEntity)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    return task


@router.post("/add")
def create_task(request, payload: TaskRequestEntity):
    """
    Endpoint para criar uma task no banco
    """
    task = Task.objects.create(**payload.dict())
    #try:
    return {"id: ", task.id}
    # except:
    #     raise ServiceUnavailableError