from django.urls import path
from .views import (
    RegisterManagerView,
    ConfirmEmailView,
    LoginManagerView,
    ManagerRUDView,
    RequestPasswordResetView,
    ResetPasswordConfirmView,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"manager", ManagerRUDView, basename="manager")


app_name = "managers"
urlpatterns = [
    path("register/manager/", RegisterManagerView.as_view(), name="register_manager"),
    path("login/manager/", LoginManagerView.as_view(), name="login_manager"),
    path(
        "confirm-email/<str:token>/", ConfirmEmailView.as_view(), name="confirm_email"
    ),
    path(
        "reset-password/manager/",
        RequestPasswordResetView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password-confirm/manager/<str:uidb64>/<str:token>/",
        ResetPasswordConfirmView.as_view(),
        name="reset-password-confirm",
    ),
] + router.urls
