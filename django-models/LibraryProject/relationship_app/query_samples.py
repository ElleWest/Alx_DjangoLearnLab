import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == '__main__':
    # Create sample data
    author1 = Author.objects.create(name='George Orwell')
    book1 = Book.objects.create(title='1984', author=author1)
    
    author2 = Author.objects.create(name='J.R.R. Tolkien')
    book2 = Book.objects.create(title='The Hobbit', author=author2)

    library1 = Library.objects.create(name='Central Library')
    library1.books.add(book1, book2)

    from relationship_app.models import Librarian
    librarian1 = Librarian.objects.create(name='Mr. Smith', library=library1)

    # Run queries
    print('Books by George Orwell:', query_books_by_author('George Orwell'))
    print('Books in Central Library:', query_books_in_library('Central Library'))
    print('Librarian for Central Library:', query_librarian_for_library('Central Library'))
