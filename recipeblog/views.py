from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipeblog.models import Recipe

# Create your views here.

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html')
