from django.shortcuts import render
from django.http import HttpResponse


def title(request):
    return HttpResponse("this is my about page")
# Create your views here.
