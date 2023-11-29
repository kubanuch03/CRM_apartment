from django.contrib import admin
from .models import Apartment, Object


class ApartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number_apartment",
        "object",
        "client",
        "floor",
        "square_meter",
        "status_choice",
        "price",
        "custom_status_display",
    )
    list_filter = ["status_choice", "object"]

    def custom_status_display(self, obj):
        if obj.status_choice == "Active":
            return "-"
        elif obj.status_choice == "Reserved":
            return f"{obj.status_choice} until {obj.date}"
        elif obj.status_choice == "Purchased":
            return f"{obj.status_choice} on {obj.date}"

    custom_status_display.short_description = "Status"


class ObjectAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    list_filter = ["title"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Object, ObjectAdmin)
admin.site.register(Apartment, ApartmentAdmin)
