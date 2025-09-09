from rest_framework import serializers

from app.models import Task

# Write your serializers here


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
