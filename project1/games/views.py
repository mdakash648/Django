from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print(request):
    return HttpResponse("this is my first django project")

def about(request):
    return HttpResponse("<h1>this is my about page</h1>")
