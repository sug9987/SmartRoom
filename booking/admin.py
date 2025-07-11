# Register your models here.

from django.contrib import admin
from .models import Room, Booking

# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'capacity')

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('room', 'user', 'start_time', 'end_time', 'created_at')
#     list_filter = ('room',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')  # <-- Just added this

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'start_time', 'end_time', 'created_at')
    list_filter = ('room', 'start_time')  # <-- Added start_time filter
    search_fields = ('room__name', 'user__username')  # <-- Added search

from django.contrib import admin
from .models import Room, Booking, UserProfile  # Add your models here

# admin.site.register(Room)
# admin.site.register(Booking)
admin.site.register(UserProfile)
