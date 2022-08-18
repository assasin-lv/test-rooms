from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
# Create your views here.

from .models import Room, Event, Reservation
from .serializers import EventSerializer
from businessEvent.constanst import *

class createRoom(GenericAPIView):
    def get(self, request, *args, **kwargs):
        capacity = request.GET.get("capacity")
        name = request.GET.get("name")

        if not capacity and not name:
            return Response(data={"message": "NO-OK"}, status=500)
        room = Room()
        room.name = name
        room.capacity = capacity
        room.save()

        return Response(data={"message": "Success"}, status=200)

class createEvent(GenericAPIView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get("name")
        type_event = request.GET.get("type_event")
        room_id = request.GET.get("room")
        user_id = request.GET.get("user")

        if not room_id and not name and not type_event and not user_id:
            return Response(data={"message": "NO-OK"}, status=500)
        
        exists_event = Event.objects.filter(room_id=room_id)
        if exists_event:
            return Response(data={"message": "The room have a event"}, status=500)

        event = Event()
        event.name = name
        event.type_event = type_event
        event.room_id = room_id
        event.user_id = user_id
        event.save()

        return Response(data={"message": "Success"}, status=200)


class dropRoom(GenericAPIView):
    def get(self, request, *args, **kwargs):
        room_id = request.GET.get("room")
        if not room_id:
            return Response(data={"message": "Room not found",}, status=400)

        event = Event.objects.filter(room_id=room_id).count()
        
        if event == 0:
            Room.objects.filter(pk=room_id).delete()
            return Response(data={"message": f"Rooms drops",}, status=200)
        
        return Response(data={"message": "No drops",}, status=200)


class createReservation(GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user")
        event_id = request.GET.get("event")

        if not user_id and not event_id:
            return Response(data={"message": "User_id not  found or event_id not found",}, status=400)

        event = Event.objects.filter(pk=event_id).first()

        if event.type_event == TYPE_PRIVATE and not event.created_by == user_id:
            return Response(data={"message": "The event is private",}, status=400)

        if not event.available:
            return Response(data={"message": "Event not available",}, status=400)

        exists_reservation = Reservation.objects.filter(event_id=event_id, user_id=user_id)
        if exists_reservation:
            return Response(data={"message": "The User have a reservation",}, status=400)

        reservation = Reservation()
        reservation.user_id = user_id
        reservation.event_id = event_id
        reservation.save()

        reservations = Reservation.objects.filter(event_id=event_id).count()

        if reservations == event.room.capacity:
            event.available = False
            event.save(update_fields=["available"])
        else:
            event.available = True
            event.save(update_fields=["available"])
        
        return Response(data={"message": "OK",}, status=200)


class dropReservation(GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user")
        event_id = request.GET.get("event")

        try:
            Reservation.objects.filter(event_id=event_id,user_id=user_id).delete()

            reservations = Reservation.objects.filter(event_id=event_id).count()
            event = Event.objects.filter(pk=event_id).first()

            if reservations == event.room.capacity:
                event.available = False
                event.save(update_fields=["available"])
            else:
                event.available = True
                event.save(update_fields=["available"])

        except Exception as ex:
            return Response(data={"message": "NO-OK",}, status=400)
        return Response(data={"message": "OK",}, status=200)



class listEventAvailables(GenericAPIView):
    def get(self, request, *args, **kwargs):

        events = Event.objects.filter(type_event=TYPE_PUBLIC, available=True).select_related("room")
        items = EventSerializer(events, many=True)
        return Response(data={"message": "OK", "data": items.data}, status=200)




        