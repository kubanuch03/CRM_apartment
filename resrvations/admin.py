from django.contrib import admin

from .models import Reservation
from apartments.models import Apartment

from datetime import date


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "apartment", "client", "end_date")

    # вывод  со статусом Active
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "apartment":
            kwargs["queryset"] = Apartment.objects.filter(status_choice="Active")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Reservation, ReservationAdmin)
