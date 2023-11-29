from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()


app_name = "clients"
urlpatterns = [

    path("list/client/", ClientListView.as_view(), name="list_client"),
    path("update/client/<int:pk>/", ClientUpdateView.as_view(), name="update_client"),
    path("delete/client/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
    
    path("register/client/", RegisterClientView.as_view(), name="register_client"),
    path("login/client/", LoginClientView.as_view(), name="login_client"),
    path(
        "confirm-email/<str:token>/", ConfirmEmailView.as_view(), name="confirm_email"
    ),
    path(
        "reset-password/client/",
        RequestPasswordResetView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password-confirm/client/<str:uidb64>/<str:token>/",
        ResetPasswordConfirmView.as_view(),
        name="reset-password-confirm",
    ),
] + router.urls
