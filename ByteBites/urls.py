# created this file to add the urls for the ByteBites app
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView, get_recipe, like_recipe, dislike_recipe, save_recipe

urlpatterns = [
    path('', views.home, name='home'),
    # path('recipe/', views.recipes, name='recipe'),
    path('post_its/', views.post_its, name='post-its'),
    path('signup/', views.user_signup, name='signup'),
    #path('signup/', SignUpView.as_view(), name='signup'),
    #path('login/', views.login, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('recipe_pg/', views.recipepg, name='recipe_pg'),
    path('recipe/<int:recipe_id>/', views.get_recipe, name='get_recipe'),
    path('recipe/<int:recipe_id>/like/', views.like_recipe, name='like_recipe'),
    path('recipe/<int:recipe_id>/dislike/', views.dislike_recipe, name='dislike_recipe'),
    path('recipe/<int:recipe_id>/save/', views.save_recipe, name='save_recipe'),
]
