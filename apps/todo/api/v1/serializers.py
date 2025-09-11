from rest_framework import serializers

from apps.todo.models import Task, User, Log

# Write your serializers here


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.values_list("id", flat=True),
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"


class LogSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.values_list("id", flat=True),
        required=False,
    )

    class Meta:
        model = Log
        fields = "__all__"
