from rest_framework import status
from rest_framework.response import Response

from base.api.v1.views import BaseAV

from apps.core.choices import StatusChoices

from apps.todo.models import Task
from apps.todo.api.v1.serializers import TaskSerializer

# Write your views here


class TodoAV(BaseAV):
    def get_instance(self, id):
        return Task.objects.filter(id=id, user_id=self.request.user.id).first()  # type: ignore

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
        data.update(
            {
                "user_id": request.user.id,
            }
        )

        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        data = request.data

        id = data.pop("id")
        instance = self.get_instance(id=id)
        if instance is None:
            response = {
                "msg": "Either no todo is created or access denied",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(instance, data=data, partial=True)

        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data

        id = data.pop("id")
        data = {
            "status": StatusChoices.DELETED,
        }
        instance = self.get_instance(id=id)
        if instance is None:
            response = {
                "msg": "No todo found",
            }
            return Response(response, status=status.HTTP_409_CONFLICT)

        serializer = TaskSerializer(instance, data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
