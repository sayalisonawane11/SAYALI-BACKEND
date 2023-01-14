from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    image_url = models.ImageField( blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="recipe")

   

class Ingredients(models.Model):
    ingredient_id = models.BigAutoField(primary_key = True)
    items = models.CharField(max_length=50)
    amount = models.IntegerField()
    unit = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "ingredient")

class Process(models.Model):
    process_id = models.BigAutoField(primary_key = True)
    step = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "process")