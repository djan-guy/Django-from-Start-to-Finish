from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def mindfulness(request):
    return render(request, 'mindfulness.html')

def about(request):
    return render(request, 'about.html')