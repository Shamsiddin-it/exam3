from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="start_loc")
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="end_loc")
    date = models.DateField()  
    seats_available = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return f"{self.start_location} to {self.end_location} on {self.date}"
    def book_seat(self):
        if self.seats_available > 0:
            self.seats_available -= 1
            self.save()
            return True
        return False


class Booking(models.Model):
    trip = models.ForeignKey("hamsafar.Trip", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f"{self.user.name} booked {self.seats_booked} seats for {self.trip}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f"Review for {self.trip} by {self.user.name} ({self.rating} stars)"


