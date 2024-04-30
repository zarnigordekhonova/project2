from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_info(request):
    return HttpResponse('Which type of ticket do you want to buy?')