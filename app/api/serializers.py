from rest_framework import serializers

from app.models import Task, User, Logs, TableInfo

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
    table_details_id = serializers.PrimaryKeyRelatedField(
        queryset=TableInfo.objects.values_list("id", flat=True),
        required=False,
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.values_list("id", flat=True),
        required=False,
    )

    class Meta:
        model = Logs
        fields = "__all__"
