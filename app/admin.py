from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Player)
admin.site.register(TimeSlot)
admin.site.register(Turf)
admin.site.register(Booking)
admin.site.register(Payment)