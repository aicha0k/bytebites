from django.db import models

# Create your models here.
class Recipe(models.Model):
    DIFFICULTY = [
        ('F', 'Fácil'),
        ('M', 'Médio'),
        ('D', 'Difícil')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    servings = models.IntegerField()
    prep_time = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    instructions = models.TextField()
    #image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now_add=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class RecipeIngredient(models.Model):
    quant = models.CharField(max_length=10)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    date_reg = models.DateTimeField(auto_now_add=True)

class Likes(models.Model):  # user can like or dislike a recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    like = models.BooleanField()

class Save(models.Model):   # user can save a recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

