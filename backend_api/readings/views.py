from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Books
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

