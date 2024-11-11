from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trip, Booking, Review, Location

class HomePage(TemplateView):
    template_name = 'home.html'

class TripCreateView( CreateView):
        model = Trip
        fields = ['start_location','end_location', 'date', 'seats_available', 'description']
        template_name = 'create_trip.html'
        success_url = reverse_lazy('trip_list')
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

class TripModelDeleteView(DeleteView):
    model = Trip
    template_name = "trip_delete.html"
    success_url = reverse_lazy('trip_list')  

class TripListView(ListView):
    model = Trip
    template_name = 'trip_list.html'
    context_object_name = 'trips'

class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip_detail.html'
    context_object_name = 'trip'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trip_book"] = Booking.objects.filter(trip = self.kwargs["pk"])
        return context
    
    success_url = reverse_lazy('trip_list')
    
class LocationCreateView(CreateView):
    model = Location
    template_name = "location_create.html"
    fields = ['name', 'description']
    success_url = "home"



class BookingListView(ListView):
    model = Booking
    template_name = "trip_detail.html"

class BookingDetailView(DetailView):
    model = Booking
    template_name = "booking_detail.html"
    context_object_name = "booking"

class BookingCreateView(CreateView):
    model = Booking
    template_name = "booking_create.html"
    fields = ['trip', 'user', 'seats_booked']
    success_url = reverse_lazy("trip_list")

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['seats_booked']
    template_name = 'booking_update.html'
    success_url = reverse_lazy('trip_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('trip_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Incorrect data'})
    return render(request, 'login.html')
    


def user_logout(request):
    logout(request)
    return redirect('home')


