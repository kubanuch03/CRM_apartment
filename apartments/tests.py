from django.test import TestCase
from .models import Apartment


class ApartmentTest(TestCase):

    def setUp(self) -> None:
        self.apartment = Apartment.objects.create(
            number_apartment = 4,
            # object = 2,
            floor = 4,
            square_meter = 132,
            status_choice = 'Active',
            price = 320000,
            
        )

    def test_apartment_creation(self):
        self.assertEqual(self.apartment.number_apartment,4)
        # self.assertEqual(self.apartment.object,2)
        self.assertEqual(self.apartment.floor,4)
        self.assertEqual(self.apartment.square_meter,132)
        self.assertEqual(self.apartment.status_choice,'Active')
        self.assertEqual(self.apartment.price,320000)