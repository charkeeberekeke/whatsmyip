from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    ip = request.META["REMOTE_ADDR"]
    return HttpResponse("Your IP address is " + ip)

