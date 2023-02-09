from django.db import models





class BookingTable(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=10)
    BookingDate = models.DateField()

    def __str__(self) -> str:
        return self.Name


class MenuTable(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField(default=5)

    def __str__(self) -> str:
        return self.Title







