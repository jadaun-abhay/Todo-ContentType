from base.api.v1.serializers import BaseSerializer

from apps.core.models import User

# Write your serializers here


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = "__all__"
