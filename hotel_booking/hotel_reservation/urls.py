from django.urls import path
from . import views


urlpatterns = [
    path('hotels/', views.HotelList.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', views.HotelDetail.as_view(), name='hotel-detail'),
    path('roomtypes/', views.RoomTypeList.as_view(), name='roomtype-list'),
    path('roomtypes/<int:pk>/', views.RoomTypeDetail.as_view(), name='roomtype-detail'),
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
]
