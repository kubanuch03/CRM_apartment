# Generated by Django 4.2.7 on 2023-11-28 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
        ("resrvations", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.client",
            ),
        ),
    ]
