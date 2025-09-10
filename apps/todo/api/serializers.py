from django.forms.models import model_to_dict

from rest_framework import serializers

from todo.models import Task, User, Logs, TableInfo

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

    def update(self, instance, validated_data):
        old_value = model_to_dict(instance=instance)
        instance.description = validated_data.get("description", instance.description)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        new_value = model_to_dict(instance=instance)

        for field in new_value.keys():
            if old_value.get(field) != new_value.get(field):
                setattr(self, "new_dict", old_value.get(field))
                setattr(self, "new_dict", new_value.get(field))

        return instance
