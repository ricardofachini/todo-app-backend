from profiles.models import Profiles
from typing import Optional

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ninja import Router
from ninja.errors import HttpError

from auth.api.entity import SignupSchema

router = Router()


@router.post("/signup")
async def signup(request, payload: SignupSchema, image: Optional[str] = None):
    if User.objects.filter(email=payload.username).exists():
        raise HttpError(400, "User already exists")

    if User.objects.filter(email=payload.email).exists():
        raise HttpError(400, "Email already exists")

    user = User.objects.create(
        username=payload.username,
        email=payload.email,
        password=make_password(payload.password),
    )

    profile = Profiles.objects.create(user=user, image=image)

    return {"message": "User created successfully", "user": user.username}
