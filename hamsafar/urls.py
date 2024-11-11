from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('trips/', TripListView.as_view(), name='trip_list'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('create_trip/', TripCreateView.as_view(), name='trip_create'),
    path('create_location/', LocationCreateView.as_view(), name='location_create'),
    path("booking/<int:pk>/", BookingCreateView.as_view(), name = "booking_create"),
    path("bookingn/<int:pk>/", BookingDetailView.as_view(), name = "booking_detail"),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
]
