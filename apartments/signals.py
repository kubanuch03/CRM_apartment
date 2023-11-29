from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from resrvations.models import Reservation
from apartments.models import Apartment
from datetime import datetime, timedelta


@receiver(post_delete, sender=Reservation)
def update_apartment_on_reservation_delete(sender, instance, **kwargs):
    apartment = instance.apartment
    apartment.status_choice = "Active"
    apartment.date = None
    apartment.client = None
    apartment.save()


@receiver(post_save, sender=Reservation)
def update_apartment_on_reservation_save(sender, instance, **kwargs):
    if instance.apartment:
        instance.apartment.status_choice = "Reserved"
        instance.apartment.date = instance.end_date
        instance.apartment.client = instance.client

        if not instance.end_date:
            instance.end_date = datetime.now() + timedelta(days=7)

        instance.apartment.save()
