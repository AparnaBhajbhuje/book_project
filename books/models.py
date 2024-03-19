from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    # Define other fields and relationships

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Define other fields
