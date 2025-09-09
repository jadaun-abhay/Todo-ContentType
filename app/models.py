from django.contrib.auth.models import AbstractUser
from django.db import models

from app.choices import StatusChoices

# Create your models here.


class BaseModel(models.Model):
    status = models.IntegerChoices(choices=StatusChoices, default=StatusChoices.CREATED)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    pass


class Task(BaseModel):
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )
