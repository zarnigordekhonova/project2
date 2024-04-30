from django.urls import path
from tickets.views import get_info

urlpatterns = [
    path('', get_info)
]