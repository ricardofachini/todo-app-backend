from profiles.models import Profiles
from typing import Optional

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ninja import Router, UploadedFile, Form
from ninja.errors import HttpError

from auth.api.entity import SignupSchema

router = Router()


@router.post("/signup")
def signup(request, payload: SignupSchema = Form(...), image: Optional[UploadedFile] = None):
    if User.objects.filter(email=payload.username).exists():
        raise HttpError(400, "User already exists")

    if User.objects.filter(email=payload.email).exists():
        raise HttpError(400, "Email already exists")

    user = User.objects.create(
        username=payload.username,
        email=payload.email,
        password=make_password(payload.password),
    )

    profile = Profiles.objects.update_or_create(user=user, defaults={
            'bio': payload.bio or '',
            'avatar': image if image else None})

    return {"message": "User created successfully", "user": user.username}
