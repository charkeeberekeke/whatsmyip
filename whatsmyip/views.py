from django.shortcuts import render
from django.http import HttpResponse
import GeoIP
from dns import resolver,reversename

# Create your views here.

def index(request):
    ip = request.META["REMOTE_ADDR"]
    country = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE).country_name_by_addr(ip)
    if country:
	fr = "from " + country
    else:
        fr = ""
    try:
        addr = reversename.from_address(ip)
        name = str(resolver.query(addr,"PTR")[0]) + "( " + ip + " ) "
    except (resolver.NXDOMAIN, resolver.NoAnswer): # no reverse dns lookup match
        name = ip

    return HttpResponse("Hello " + name + fr)
