from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.customer_form, name='customer_form'),
]