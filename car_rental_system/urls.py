from django.urls import path
from .views import *


app_name = 'car_rental_system'

urlpatterns = [
    path('', render_react)
]
