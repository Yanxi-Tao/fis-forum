from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello here is the django page we created")
# Create your views here.
