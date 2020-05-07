from django.urls import path
from hotel_app import views


urlpatterns = [
    path('', views.index, name='index'),
]