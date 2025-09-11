from django.urls import path

from apps.core.api.v1.views import SignUp, AuthAV

# Write your urls here

urlpatterns = [
    path(
        "sign-up/",
        SignUp.as_view(),
    ),
    path(
        "auth/",
        AuthAV.as_view(),
    ),
]
