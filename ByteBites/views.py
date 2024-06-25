from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from .models import Post_it
from .models import Recipe, Likes
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    return render(request, 'index.html')

def post_its(request):
    my_posts = Post_it.objects.all().order_by('-created_on')
    return render(request, 'post_its.html', {'my_posts': my_posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipe': recipes})

def get_recipe(request): 
    recipe_id = request.GET.get('recipe_id') 
    recipe = Recipe.objects.get(pk=recipe_id)
    return HttpResponse(json.dumps(recipe), content_type='application/json')

def recipepg(request):
    return render(request, 'recipespg.html', {'recipes_pg': recipepg})

def like_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user
    like, created = Likes.objects.get_or_create(user=user, recipe=recipe)
    if not created:
        like.like = not like.like
        like.save()
