from django.db import models

from app.enums import Status

# Write your managers here


class DeleteStatusManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().exclude(status=Status.DELETED)
