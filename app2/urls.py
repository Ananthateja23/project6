from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('thor/',thor,name='thor'),
    path('wakanda/',wakanda,name='wakanda'),
]