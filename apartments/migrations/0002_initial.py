# Generated by Django 4.2.7 on 2023-11-28 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apartments", "0001_initial"),
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clients.client",
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="object",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="apartments.object",
            ),
        ),
        migrations.AddIndex(
            model_name="apartment",
            index=models.Index(fields=["id"], name="apartments__id_8e1a9b_idx"),
        ),
        migrations.AddIndex(
            model_name="apartment",
            index=models.Index(
                fields=["number_apartment"], name="apartments__number__b92b0b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="apartment",
            index=models.Index(
                fields=["-created_at"], name="apartments__created_929d58_idx"
            ),
        ),
    ]