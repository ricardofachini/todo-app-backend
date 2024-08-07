from ninja import Router

from ..models import Task
from .entity import TaskRequestSchema


router = Router()


@router.get("/list")
def list_all_tasks(request):
    return [
        {"id": e.id, "nome": e.title}
        for e in Task.objects.all()
    ]

@router.post("/add")
def create_task(request, payload: TaskRequestSchema):
    """
    Endpoint para criar uma task no banco
    """
    task = Task.objects.create(**payload.dict())
    return {"id: ", task.id}