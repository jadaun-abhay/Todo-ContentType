from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.core.models import BaseModel, User


# Create your models here.


class Task(BaseModel):
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )


class Log(BaseModel):
    old_value = models.JSONField()
    new_value = models.JSONField()
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="logs",
    )
