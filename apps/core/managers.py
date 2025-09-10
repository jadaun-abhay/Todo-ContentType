from django.db.models import Manager
from django.db.models.query import QuerySet

from apps.core.choices import StatusChoices

# Write your managers here


class DeleteChoiceManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().exclude(status=StatusChoices.DELETED)
