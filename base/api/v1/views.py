from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from base.api.v1.constants import success_status
from base.api.v1.permissions import AuthPermission

# Write your views here


class BaseAV(APIView):
    authentication: bool | dict

    permission_classes = [
        AuthPermission,
    ]

    def success(self, response):
        status = success_status.get(self.request.method.lower())  # type: ignore
        if isinstance(response, dict):
            return Response(
                response,
                status=status,
            )

        return Response(
            {
                "msg": response,
            },
            status=status,
        )

    def fail(self, response, status=status.HTTP_400_BAD_REQUEST):
        if isinstance(response, dict):
            return Response(response, status=status)

        return Response(
            {
                "msg": response,
            },
            status=status,
        )
