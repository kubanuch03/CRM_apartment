from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import login, authenticate
from .models import CustomUser
from .serializers import CustomUserSerializer


class LoginUserView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if email and password:
            user = authenticate(
                email=email,
                password=password,
                backend="users.backends.MultiUserAuthBackend",
            )

            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "user_id": user.id,
                        "email": user.email,
                        "username": user.username,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "detail": "Authentication failed. User not found or credentials are incorrect."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid input. Both email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
