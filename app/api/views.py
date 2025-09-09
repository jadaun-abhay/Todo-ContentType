import base64

from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.enums import Status
from app.models import User, Task
from app.api.serializers import TaskSerializer

# Write your views here


class SignUpAV(APIView):
    authentication_classes = []

    def post(self, request):
        data = request.data
        password = data.pop("password")
        user = User(**data)
        user.set_password(password)
        user.save()
        response = {
            "msg": "User registered successfully.",
        }
        return Response(response, status=status.HTTP_201_CREATED)


class AuthAV(APIView):
    authentication_classes = []

    def decrypt_meta(self, meta):
        header, value = meta.split(" ")
        decoded_credentials = base64.b64decode(value).decode("utf-8")
        credentials = decoded_credentials.split(":")
        return {
            "username": credentials[0],
            "password": credentials[1],
        }

    def get(self, request):
        response = {
            "msg": "Login Successfull",
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        meta_data = request.META["HTTP_AUTHORIZATION"]
        print("hello", meta_data)
        credentials = self.decrypt_meta(meta=meta_data)
        if credentials.get("username") and credentials.get("password"):
            user = authenticate(request, **credentials)
            if user is not None:
                login(request, user)
                response = {
                    "msg": "Login Successfull.",
                }
                return Response(response, status=status.HTTP_200_OK)
            response = {
                "msg": "invalid credentials",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        response = {
            "msg": "username or password is not provided",
        }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class TodoAV(APIView):
    def get_instance(self, id):
        return Task.objects.filter(id=id).first()

    def get(self, request):
        params = request.query_params

        id = params.get("id")

        if id is None:
            queryset = Task.objects.filter(user=request.user)
            serializer = TaskSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        instance = self.get_instance(id=id)
        serializer = TaskSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data

        id = data.get("id")
        instance = self.get_instance(id=id)

        serializer = TaskSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data

        id = data.get("id")
        instance = self.get_instance(id=id)

        serializer = TaskSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
