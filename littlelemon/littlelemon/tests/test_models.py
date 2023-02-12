from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
    #menu table

    def test_add_into_model(self):
        menuItem = models.MenuTable
        item = menuItem.objects.create(
            title ="IceCream",
            Price = 80,
            Inventory = 100
            )
        # self.assertEqual(item, "IceCream : 80")
        

