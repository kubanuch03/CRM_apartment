from rest_framework import routers
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register(r"apartment", ApartmentViewSet, basename="apartment")
router.register(r"object", ObjectViewSet, basename="object")


urlpatterns = [] + router.urls
