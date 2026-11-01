from django.urls import path
from . import views

# Maps the /books/ URL to the BookList view
urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    # Route for single-book operations using the book's primary key
path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
]