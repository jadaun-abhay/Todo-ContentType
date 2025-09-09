from django.db.models import Choices

# Write your choices here


class StatusChoices(Choices):
    DELETED = 0
    CREATED = 1
    UPDATED = 2
