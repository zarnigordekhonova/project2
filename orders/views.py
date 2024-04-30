from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_info_user(request):
    return HttpResponse('Enter the country name you would like to go: ')