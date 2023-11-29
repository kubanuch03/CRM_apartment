from django.db import models
from users.models import CustomUser


class Client(CustomUser):
    is_client = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
