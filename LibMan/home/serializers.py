from django.db import models
from rest_framework import serializers
from .models import Book,Review

# Create your models here
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'text', 'rating']