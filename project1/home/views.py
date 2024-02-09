from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is my home page")

def content(request):
    return HttpResponse("This is my home page content")
# Create your views here.
