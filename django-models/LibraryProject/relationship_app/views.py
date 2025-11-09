from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """
    A function-based view that lists all books.
    """
    books = Book.objects.all()
    text = ""
    for book in books:
        text += f"{book.title} by {book.author.name}\\n"
    return HttpResponse(text, content_type='text/plain')

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
