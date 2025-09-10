from django.urls import path

from todo.api.views import AuthAV, SignUpAV, TodoAV

# Write your urls here

urlpatterns = [
    path(
        "sign-up/",
        SignUpAV.as_view(),
    ),
    path(
        "auth/",
        AuthAV.as_view(),
    ),
    path(
        "todo/",
        TodoAV.as_view(),
    ),
]
