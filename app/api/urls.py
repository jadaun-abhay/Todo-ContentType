from django.urls import path

from app.api.views import AuthAV, SignUpAV

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
]
