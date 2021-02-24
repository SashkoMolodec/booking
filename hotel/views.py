from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hotels_view(*args, **kwargs):
    return HttpResponse("<h1>Hotels Page</h1>")


def single_hotel_view(*args, **kwargs):
    return HttpResponse("<h1>Single Hotel page</h1>")
