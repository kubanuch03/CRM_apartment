from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"reservation", CRUDReservationViewSet, basename="reservation")


urlpatterns = [] + router.urls
