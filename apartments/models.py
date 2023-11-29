from django.db import models
from django.utils.text import slugify

from datetime import datetime, timedelta

from clients.models import Client


class Object(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Object"
        verbose_name_plural = "Objects"
        ordering = ["title"]
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["title"]),
        ]


class Apartment(models.Model):
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Reserved", "Reserved"),
        ("Purchased", "Purchased"),
        ("Installment", "Installment"),
        ("Barter", "Barter"),
        ("Cancel", "Cancel"),
    ]

    number_apartment = models.IntegerField(default=0, unique=True)
    object = models.ForeignKey(Object, on_delete=models.SET_NULL, null=True)
    floor = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    square_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status_choice = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default="Active"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(null=True, blank=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.number_apartment)

        if self.status_choice == "Reserved" and not self.date:
            self.date = datetime.now() + timedelta(days=7)

        elif self.status_choice == "Purchased" and not self.date:
            self.date = datetime.now

        super().save(*args, **kwargs)

    def __str__(self):
        # Возвращаем строку с объединенным статусом и временем (если есть)
        if self.status_choice == "Reserved":
            return f"{self.number_apartment} - {self.status_choice} until {self.date}"
        elif self.status_choice == "Purchased":
            return f"{self.number_apartment} - {self.status_choice} on {self.date}"
        else:
            return f"{self.number_apartment} - {self.status_choice}"

    # быстрый поиск по индексу
    class Meta:
        ordering = ["number_apartment"]
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["number_apartment"]),
            models.Index(fields=["-created_at"]),
        ]
