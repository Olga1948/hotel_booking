from rest_framework import generics
from .models import Hotel, RoomType, Booking
from .serializers import HotelSerializer, RoomTypeSerializer, BookingSerializer
from django.views import View
from django.shortcuts import render


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomTypeList(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class AllHotelsView(View):
    def get(self, request, *args, **kwargs):
        hotels = Hotel.objects.all()
        return render(request, 'all_hotels.html', {'hotels': hotels})
