from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import Post_it
from .models import Recipe, Likes, Save, User
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def post_its(request):
    my_posts = Post_it.objects.all().order_by('-created_on')
    return render(request, 'post_its.html', {'my_posts': my_posts})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

def user_signup(request):
    if request.method != 'POST':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    form = SignUpForm(request.POST)
    # if form.is_valid()==False:
    #     raise ValidationError('Invalid form')
    try:
        user = form.save()
        user.username = form.cleaned_data.get('username')
        #password = user.password(form.cleaned_data.get('password1'))   Use set_password to hash the password
        password = form.cleaned_data.get('password1')
        confirm_password = form.cleaned_data.get('password2')
        if user.password != confirm_password:
            raise ValidationError('Passwords do not match')
        user.set_password(password)
        user.save()
        login(request, user)
        print('User created successfully')
        return redirect('home')
    except Exception as e:
        print("Error: ", str(e))
        form.add_error(None, 'An unexpected error occurred: {}'.format(str(e)))

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid username and password'})

def user_logout(request):
    logout(request)
    return redirect('home')

def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipe': recipes})

def get_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    #return HttpResponse(json.dumps(recipe), content_type='application/json')
    return render(request, 'recipe.html', {'recipe': recipe})

def recipepg(request):
    # falta .all()
    recipes_pg = Recipe.objects.all()
    return render(request, 'recipespg.html', {'recipes_pg': recipes_pg})

@login_required
def like_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user
    like, created = Likes.objects.get_or_create(user=user, recipe=recipe)
    if not created:
        if like.like:
            like.delete()
        else:
            like.like = True
            like.save()
    return JsonResponse({{'likes_count': Likes.objects.filter(recipe=recipe, like=True).count()}})

@login_required
def dislike_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user
    like, created = Likes.objects.get_or_create(user=user, recipe=recipe)
    if not created:
        if not like.like:
            like.delete()
        else:
            like.like = False
            like.save()
    return JsonResponse({'dislikes_count': Likes.objects.filter(recipe=recipe, like=False).count()})

@login_required
def save_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user
    favorite, created = Save.objects.get_or_create(user=user, recipe=recipe)
    if not created:
        favorite.delete()
    return JsonResponse({'favorite_count': Save.objects.filter(recipe=recipe).count()})