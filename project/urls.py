from django.urls import path
from showroom import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/<int:pk>/buy/', views.buy_car, name='buy_car'),
    path('tradein/', views.tradein, name='tradein'),
]
