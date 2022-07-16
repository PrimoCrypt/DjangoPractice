from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "FirstApp/index.html")

def primo(request):
    return HttpResponse("Hello World, it is Primo here")

def greet(request, name):
    return HttpResponse(f"Good Day {name.capitalize()} you're welcome")
