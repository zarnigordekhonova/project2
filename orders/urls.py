from django.urls import path
from orders.views import get_info_user

urlpatterns = [
    path('', get_info_user)
]