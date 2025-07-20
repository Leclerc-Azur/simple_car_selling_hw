
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('add/', views.add_car, name='add_car'),
]