# Generated by Django 4.2.7 on 2023-11-28 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("resrvations", "0001_initial"),
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="clients.client"
            ),
        ),
    ]