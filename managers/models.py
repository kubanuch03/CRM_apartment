from django.db import models
from users.models import CustomUser


class Manager(CustomUser):
    is_manager = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    amount_deals = models.IntegerField(default=0)
