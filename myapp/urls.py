from django.urls import path
from . import views
from .views import log_view
from .views import about
from .views import menu
from .views import menu_card


urlpatterns = [
    path('form/', views.customer_form, name='customer_form'),
    path('form/', views.form_view, name='form_view'),
    path('', log_view, name='log_form'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('menu_card/', menu_card, name='menu_card'),
    path('', views.home, name='home'),
] 




