from django.urls import path

from apps.todo.api.v1.views import TodoAV

# Write your urls here

urlpatterns = [
    path(
        "task/",
        TodoAV.as_view(),
    ),
]
