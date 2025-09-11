from rest_framework import serializers

from apps.core.models import BaseModel

# Write your serializers here


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        fields = kwargs.get("fields")
        exclude = kwargs.get("exclude")

        super(BaseSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            pass
