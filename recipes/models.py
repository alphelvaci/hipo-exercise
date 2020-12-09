from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Count

class Ingredient(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name

    def use_count(self):
        return Ingredient.objects.filter(name=self.name).annotate(count=Count('recipe')).first().count

class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='%Y/%m/')
    instructions = models.TextField()
    difficulty_choices = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]
    difficulty = models.CharField(max_length=10, choices=difficulty_choices, default="easy")
    ingredients = models.ManyToManyField(Ingredient)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title