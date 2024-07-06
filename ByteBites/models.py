from django.db import models
import datetime as dt
from django.utils import timezone

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
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')

    def __str__(self):
        return self.name
    def published_recently(self):
        return self.date_added >= timezone.now() - dt.timedelta(days=1)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quant = models.CharField(max_length=30, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.ingredient.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    date_reg = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.password = self.password
        super(User, self).save(*args, **kwargs)

class Likes(models.Model):  # user can like or dislike a recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    like = models.BooleanField()

class Save(models.Model):   # user can save a recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

class Post_it(models.Model): # admin can make tiny posts unrelated to recipes
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Criado em", help_text="Data e hora de criação do objeto")


    def __str__(self):
        return self.title
