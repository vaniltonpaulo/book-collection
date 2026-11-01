from rest_framework import serializers
from .models import Book


# Converts Book model instances to/from JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'