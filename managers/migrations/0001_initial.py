# Generated by Django 4.2.7 on 2023-11-28 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("is_manager", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=False)),
                ("amount_deals", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
            bases=("users.customuser",),
        ),
    ]