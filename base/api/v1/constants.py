from rest_framework import status

# Write your constants here

success_status = {
    "get": status.HTTP_200_OK,
    "post": status.HTTP_201_CREATED,
    "put": status.HTTP_200_OK,
    "patch": status.HTTP_200_OK,
    "delete": status.HTTP_200_OK,
}
