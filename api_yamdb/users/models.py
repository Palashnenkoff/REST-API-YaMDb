import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(
        max_length=500,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
    )

    class UserRole:
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'admin'
        choices = [
            (USER, USER),
            (ADMIN, ADMIN),
            (MODERATOR, MODERATOR),
        ]

    role = models.CharField(
        max_length=25,
        choices=UserRole.choices,
        default=UserRole.USER,
    )
    confirmation_code = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
