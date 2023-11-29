from django.contrib import admin

from managers.models import Manager


class ManagerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone_number",
        "amount_deals",
        "created_at",
    )
    search_fields = ("username", "email", "phone_number", "created_at")
    list_filter = ("is_staff", "created_at")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "username",
                    "full_name",
                    "amount_deals",
                    "is_verified",
                    "is_manager",
                    "is_active",
                    "created_at",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "full_name",
                    "phone_number",
                ),
            },
        ),
    )
    readonly_fields = ("created_at",)


admin.site.register(Manager, ManagerAdmin)
