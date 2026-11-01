from django.shortcuts import render

# Create your views here.
#Section 3 - step 1
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


# Handles GET (list all books) and POST (create a new book)
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#section 4 - step 1
    # View for retrieving, updating, and deleting a single book
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

