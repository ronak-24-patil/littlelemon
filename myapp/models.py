from django.db import models

# Model for Menu Categories
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Menu Items
class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        MenuCategory, 
        on_delete=models.PROTECT, 
        default=None,
        related_name='category_name'  # Optional: Makes querying more intuitive
    )

    def __str__(self):
        return self.menu_item

class Customer(models.Model):
    name = models.CharField(max_length=100)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

class Logger(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    time = models.DateTimeField()
    guest_count = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name  # Display name in the admin panel
