from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from .pydantic_models import BookCreateUpdateModel, ReviewCreateModel

@api_view(['POST'])
def add_book(request):
    """
    Add a new book (title, author, publication year).
    """
    if request.method == 'POST':
        data = request.data
        book_data = BookCreateUpdateModel(**data)
        serializer = BookSerializer(data=book_data.dict())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_review(request, book_id):
    """
    Submit a review for a book (text review, rating).
    """
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        data = {'book': book.id, **request.data}
        review_data = ReviewCreateModel(**data)
        serializer = ReviewSerializer(data=review_data.dict())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_books(request):
    """
    Retrieve all books with an option to filter by author or publication year.
    """
    author = request.query_params.get('author', None)
    publication_year = request.query_params.get('publication_year', None)

    books = Book.objects.all()
    if author:
        books = books.filter(author=author)
    if publication_year:
        books = books.filter(publication_year=publication_year)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reviews(request, book_id):
    """
    Retrieve all reviews for a specific book.
    """
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    reviews = Review.objects.filter(book=book)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)