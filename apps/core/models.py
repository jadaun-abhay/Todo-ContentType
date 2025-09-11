import uuid6

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from apps.core.choices import StatusChoices
from apps.core.managers import DeleteChoiceManager

# Create your models here.


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid6.uuid6())
    status = models.IntegerField(
        choices=StatusChoices.choices,
        default=StatusChoices.CREATED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DeleteChoiceManager()

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
