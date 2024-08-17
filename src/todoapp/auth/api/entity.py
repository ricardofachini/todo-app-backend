from ninja import Schema
from pydantic import constr, EmailStr, StringConstraints
from typing import Optional, Annotated


class SignupSchema(Schema):
    username: str
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]
    bio: Optional[str] = None
    #image: Optional[str] = None
