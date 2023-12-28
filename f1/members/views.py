from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
def mainone(request):
    return HttpResponse('homepage')