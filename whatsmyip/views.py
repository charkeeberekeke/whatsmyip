from django.shortcuts import render
from django.http import HttpResponse
import GeoIP

# Create your views here.

def index(request):
    ip = request.META["REMOTE_ADDR"]
    gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
    return HttpResponse("Hello " + ip +  " from " + str(gi.country_name_by_addr(ip)))
