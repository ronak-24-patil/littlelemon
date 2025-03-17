from django.urls import path
from . import views
from .views import log_view
from .views import about

urlpatterns = [
    path('form/', views.customer_form, name='customer_form'),
    path('form/', views.form_view, name='form_view'),
    path('', log_view, name='log_form'),
    path('about/', about, name='about'),
]

