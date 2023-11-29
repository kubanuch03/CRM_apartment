from rest_framework import permissions, viewsets

from .models import Reservation
from .serializers import ReservationSerializer

class CRUDReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]


   

    