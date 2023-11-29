from django.db import models

from clients.models import Client
from apartments.models import Apartment


class Reservation(models.Model):
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, related_name="reservations"
    )
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
