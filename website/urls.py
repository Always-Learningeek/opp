#from django.urls import path
from opp.urls import *
from website.views import index_view

urlpatterns = [
    path('', index_view),
]