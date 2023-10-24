from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Game Ratings Index")

def qualquer(request):
    return HttpResponse("qualquer coisa")
