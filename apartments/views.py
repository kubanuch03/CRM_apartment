from rest_framework import viewsets

from .models import Apartment, Object
from .permissions import IsManagerOrAdmin
from .serializers import ApartmentSerializer, ObjectSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsManagerOrAdmin]

    # Фильтрация по статусам в маршрутизаторе /?status_choice=Active без слеша
    def get_queryset(self):
        status_choice = self.request.query_params.get("status", None)
        queryset = Apartment.objects.all()

        if status_choice:
            queryset = queryset.filter(status_choice__iexact=status_choice).distinct()
        return queryset


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsManagerOrAdmin]

    def get_queryset(self):
        status_choice = self.request.query_params.get("status", None)
        queryset = Object.objects.all()

        if status_choice:
            queryset = queryset.filter(status_choice__iexact=status_choice).distinct()
        return queryset