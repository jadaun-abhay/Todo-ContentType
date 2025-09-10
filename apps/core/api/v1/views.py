import base64

from django.contrib.auth import authenticate, login, logout

from rest_framework import status

from base.api.v1.views import BaseAV

from apps.core.api.v1.serializers import UserSerializer

# Write your view here


class SignUp(BaseAV):
    authentication = False

    def post(self, request):

        data = request.data

        serializer = UserSerializer(
            data=data,
        )
        if serializer.is_valid():
            serializer.save()
            self.success(response="Registration successfull !")
        self.fail(response=serializer.errors)


class AuthAV(BaseAV):
    authentication = {
        "post": False,
    }

    def decrypt_meta(self, meta):
        header, value = meta.split(" ")
        decoded_credentials = base64.b64decode(value).decode("utf-8")
        credentials = decoded_credentials.split(":")
        return {
            "username": credentials[0],
            "password": credentials[1],
        }

    def get(self, request):
        self.success(
            response=UserSerializer(
                request.user,
                fields=(
                    "uuid",
                    "email",
                    "first_name",
                    "last_name",
                ).data,  # type: ignore
            )
        )

    def post(self, request):
        meta_data = request.META["HTTP_AUTHORIZATION"]
        credentials = self.decrypt_meta(meta=meta_data)
        if credentials.get("username") and credentials.get("password"):
            user = authenticate(request, **credentials)
            if user is not None:
                login(request, user)
                self.success(response="Login Successfull !")
            self.fail(
                response="Invalid Credentials.",
                status=status.HTTP_401_UNAUTHORIZED,
            )
        self.fail(
            response="Username or Password is not provided.",
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def delete(self, request):
        logout(request)
        self.success(response="Logout Successfull !")
