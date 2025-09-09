from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from app.enums import Status
from app.managers import DeleteStatusManager

# Create your models here.


class BaseModel(models.Model):
    status = models.IntegerField(default=Status.CREATED)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = DeleteStatusManager()

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    objects = UserManager()
    pass


class Task(BaseModel):
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )


class Logs(BaseModel):
    old_value = models.TextField()
    new_value = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveBigIntegerField()
    table = GenericForeignKey()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="logs",
    )
