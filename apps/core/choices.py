from django.db import models

# Write your choices here


class StatusChoices(models.IntegerChoices):
    DELETED = 0
    CREATED = 1
    UPDATED = 2
