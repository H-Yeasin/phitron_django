from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def apphome(request):
    return HttpResponse("This is app home page")
def courses(request):
    return HttpResponse("This is courses page")
