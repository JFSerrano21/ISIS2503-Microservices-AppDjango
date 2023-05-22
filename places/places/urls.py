from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import places

urlpatterns = [
    url(r'^place/', places.PlaceList, name='placeList'),
    url(r'^place/$', csrf_exempt(places.PlaceCreate), name='placeCreate'),
]