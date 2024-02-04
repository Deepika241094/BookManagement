from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField(default=2022)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()