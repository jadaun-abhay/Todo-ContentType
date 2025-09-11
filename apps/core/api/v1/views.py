import base64

from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework.response import Response

from base.api.v1.views import BaseAV

from apps.core.api.v1.serializers import UserSerializer, AuthSerializer

# Write your view here


class SignUp(BaseAV):
    authentication = False

    def post(self, request):
        print("hello")

        data = request.data

        serializer = UserSerializer(
            data=data,
        )
        if serializer.is_valid():
            serializer.save()
            response = {
                "msg": "Registration Successful",
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthAV(BaseAV):
    authentication = {
        "post": False,
    }

    def decrypt_meta(self, meta):
        header, value = meta.split(" ")
        decoded_credentials = base64.b64decode(value).decode("utf-8")
        credentials = decoded_credentials.split(":")
        return {
            "email": credentials[0],
            "password": credentials[1],
        }

    def get(self, request):
        response = UserSerializer(
            request.user,
            fields=(
                "uuid",
                "email",
                "first_name",
                "last_name",
            ).data,  # type: ignore
        )
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        meta_data = request.META["HTTP_AUTHORIZATION"]
        credentials = self.decrypt_meta(meta=meta_data)
        if credentials.get("email") and credentials.get("password"):
            serializer = AuthSerializer(
                data=credentials,
                context={
                    "request": request,
                },
            )
            if serializer.is_valid():
                login(request, serializer.validated_data.get("user"))  # type: ignore
                response = {
                    "msg": "Login Successful !",
                }
                return Response(response, status=status.HTTP_200_OK)
            response = {
                "msg": "Invalid Credentials.",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        response = {
            "msg": "Username or Password is not provided",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        logout(request)
        response = {
            "msg": "Logout successfull !",
        }
        return Response(response, status=status.HTTP_200_OK)
