from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('park', views.ParkCar.as_view(), name='park-car'),
    path('unpark', views.UnparkCar.as_view(), name='unpark-car'),
    path('getparkinginfo', views.GetCarSlotInfo.as_view(), name='getparkinginfo'),
]