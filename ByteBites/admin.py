from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, User, Likes, Post_it
# Register your models here.
# use admin interface to add edit and delete recipes, only admin can access this

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(User)
admin.site.register(Likes)
admin.site.register(Post_it)

# Save model is not registered as it is not required to be accessed by admin

# Path: ByteBites/models.py
# Compare this snippet from ByteBites/models.py:
# from django.db import models
#