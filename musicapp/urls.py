
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home),
    path('about/',about),
    path('bollywood/',bollywood),
    path('ncs/',ncs),
    path('pop/',pop),
    path('about/bollywood/', bollywood, name='bollywood'),
    path('about/ncs/', ncs, name='ncs'),
    path('about/pop/', pop, name='pop'),

]
