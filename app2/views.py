from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def thor(request):
    return HttpResponse("<h1>Iam the son of Odin.....</h1>")
def wakanda(request):
    return HttpResponse("<h1>Iam the the black panther</h1>")