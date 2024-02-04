from django.urls import path
from .views import *

urlpatterns = [
    path('add_book/',add_book, name="add_book"),
    path('submit_review/',submit_review, name="submit_review"),
    path('get_books/',get_books, name="get_books"),
    path('get_reviews',get_reviews, name="get_reviews"),
]
