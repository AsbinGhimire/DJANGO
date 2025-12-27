from .views import bmi_calculator
from django.urls import path

urlpatterns = [

    path('',bmi_calculator, name='bmi_calculator'),
]
