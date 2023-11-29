from rest_framework import serializers

from .models import Reservation
from users.models import CustomUser
from clients.models import Client

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id","apartment", "client", "description", "start_date", "end_date"]

    def create(self, validated_data):
        user = self.context['request'].user

        # Если пользователь админ или менеджер, создаем запись с полем client, равным None
        if isinstance(user, CustomUser) and (user.is_staff or user.is_superuser):
            return super().create(validated_data)
        # Если пользователь клиент, назначаем текущего пользователя как client
        elif isinstance(user, CustomUser) and hasattr(user, 'client'):
            client_instance = user.client
            validated_data['client'] = client_instance
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("Invalid user type or missing client.")

