from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    time_required = models.CharField(max_length=20)
    instructions = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_fave = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.author}"