from django.urls import path
from . import views

urlpatterns = [
    path('review_list', views.review_list, name='review_list'),
    path('add', views.add_review, name='add_review'),
]