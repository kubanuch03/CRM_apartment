from rest_framework import serializers

from .models import Apartment, Object


class ObjectSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    class Meta:
        model = Object
        fields = ["title", "slug"]




class ApartmentSerializer(serializers.ModelSerializer):
    number_apartment = serializers.IntegerField(required=True)
    floor = serializers.IntegerField(required=True)
    square_meter = serializers.IntegerField(required=True)
    status_choice = serializers.CharField(required=True)
    custom_status_display = serializers.CharField(read_only=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Apartment
        fields = [
            "id",
            "number_apartment",
            "object",
            "floor",
            "square_meter",
            "status_choice",
            "price",
            "client",
            "custom_status_display"
        ]
