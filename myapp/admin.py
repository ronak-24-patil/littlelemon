from django.contrib import admin
from .models import MenuCategory, Menu
from .models import Customer
from .models import Logger

# Register models here
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Logger)
