from django.contrib import admin
from .models import MenuCategory, Menu
from .models import Customer

# Register models here
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Customer)

