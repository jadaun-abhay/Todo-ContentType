from django.contrib.auth import authenticate

from rest_framework import serializers

from base.api.v1.serializers import BaseSerializer

from apps.core.models import User

# Write your serializers here


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def save(self):
        password = self.validated_data.pop("password")  # type: ignore

        user = User(**self.validated_data)  # type: ignore
        user.set_password(password)
        user.save()

        return user


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        request = self.context.get("request")
        user = authenticate(request, email=email, password=password)
        if user is None:
            raise serializers.ValidationError(detail="No such user")
        data["user"] = user
        return data
