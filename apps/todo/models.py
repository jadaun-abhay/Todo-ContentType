from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.todo.enums import Status
from apps.todo.managers import DeleteStatusManager

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
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )


class TableInfo(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Logs(BaseModel):
    old_value = models.JSONField()
    new_value = models.JSONField()
    table_details = models.ForeignKey(
        TableInfo,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tables",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="logs",
    )
