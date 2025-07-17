from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def jan(request):
    return HttpResponse("No sugar")


def feb(request):
    return HttpResponse("Max protien")


def mar(request):
    return HttpResponse("Sleep enough")


def apr(request):
    return HttpResponse("Read daily")