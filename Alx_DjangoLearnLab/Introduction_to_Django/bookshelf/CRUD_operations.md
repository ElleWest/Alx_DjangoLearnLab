# CRUD Operations Documentation

This file documents all CRUD operations performed on the Book model.

## Create Operation

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(f"Created book: {book}")
```

## Retrieve Operation

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Update Operation

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated book title: {book.title}")
```

## Delete Operation

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Verify deletion
books = Book.objects.all()
print(f"Remaining books: {list(books)}")
```
