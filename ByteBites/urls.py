# created this file to add the urls for the ByteBites app
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', views.recipes, name='recipe'),
    path('post_its/', views.post_its, name='post-its'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('recipe_pg/', views.recipepg, name='recipe_pg'),
    path('recipes/<int:id>/', views.recipe_detail, name='recipe_detail')
]
