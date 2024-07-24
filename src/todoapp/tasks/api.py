from ninja import Router

from .models import Task


router = Router()


@router.get("/list")
def list_all_tasks(request):
    return [
        {"id": e.id, "nome": e.title}
        for e in Task.objects.all()
    ]