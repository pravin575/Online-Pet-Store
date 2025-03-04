from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('search',views.search),
    path('details',views.product_details),

]