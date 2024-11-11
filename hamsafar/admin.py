from django.contrib import admin
from .models import *

admin.site.register(Location)
admin.site.register(Trip)
admin.site.register(Booking)
admin.site.register(Review)

