from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('tony/',tony,name='tony'),
    path('bruce/',bruce,name='bruce')
]