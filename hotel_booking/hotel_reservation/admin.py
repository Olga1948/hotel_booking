from django.contrib import admin
from .models import Hotel, Booking, RoomType


admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(RoomType)
