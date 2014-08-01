from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello cats!!")

def sound(request):
    return render_to_response("index2.html")
