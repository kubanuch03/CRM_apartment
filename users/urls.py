from django.urls import path
from .views import LoginUserView

urlpatterns = [
    # path("register/user/", RegisterManagerView.as_view(), name="register_manager"),
    path("login/user/", LoginUserView.as_view(), name="login_manager"),
]
