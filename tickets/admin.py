from django.contrib import admin
from tickets.models import Guest,Reservation,Movie

admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Guest)
