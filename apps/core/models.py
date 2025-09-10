import uuid6

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid6.uuid6())
