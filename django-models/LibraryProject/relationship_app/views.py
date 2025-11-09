from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """
    A function-based view that lists all books.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
