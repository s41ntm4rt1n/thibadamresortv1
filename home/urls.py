from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns=[
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('rooms/', rooms, name='rooms'),
    path('room/details/<slug:slug>/', RoomDetailView.as_view(), name='room_details'),
    path('gallery/', gallery, name='gallery'),
    path('services/', services, name='services'),
    path('blog/', blog, name='blog'),
    path('booking/', booking, name='booking'),
    path('newsletter/', newsletter, name='newsletter'),
    path('privacy-policy/', privacy, name='privacy'),
    path('terms-of-service/', terms, name='terms'),
    path('test/', test, name='test'),
    path('rooms/check-availability/', check_room_availability, name='check_availability'),

]