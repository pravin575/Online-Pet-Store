from django import views
from django.urls import path
from .views import return_order
from .views import return_success

urlpatterns = [
    path("return", return_order, name="return_order"),
    path('return_success',return_success, name='return_success'),
    
]
