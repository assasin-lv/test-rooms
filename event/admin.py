from django.contrib import admin

# Register your models here.

from .models import Room, Event, Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "capacity",
    )



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type_event",
        "room",
    )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event",
    )