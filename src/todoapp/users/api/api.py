from ninja import Router, Schema
from ..models import User

router = Router()

# class UserResponse(Schema):
#     name: str
#     email: str

@router.get("/")
def get_user(request):
    return [
        {"id": e.id, "nome": e.name}
        for e in User.objects.all()
    ]