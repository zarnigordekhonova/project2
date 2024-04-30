from django.contrib import admin
from tickets.models import tickets_info, available_tickets

# Register your models here.

admin.site.register(tickets_info)
admin.site.register(available_tickets)