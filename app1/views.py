from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tony(request):
    return HttpResponse("<h1>Iam the ironman......</h1>")
def bruce(request):
    return HttpResponse("<h1>Iam the Hulk.....</h1>")