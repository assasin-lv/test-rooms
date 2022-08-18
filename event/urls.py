from django.urls import path
from . import views

urlpatterns = [
    path('create-room/', views.createRoom.as_view()),
    path('create-event/', views.createEvent.as_view()),
    path('drop-room/', views.dropRoom.as_view()),

    path('reservation/', views.createReservation.as_view()),
    path('drop-reservation/', views.dropReservation.as_view()),

    path('list-availables-event/', views.listEventAvailables.as_view()),
    

]