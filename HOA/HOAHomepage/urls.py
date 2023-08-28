from django.urls import path
from .views import *

urlpatterns = [
    #se alle data
    path('', home),
]