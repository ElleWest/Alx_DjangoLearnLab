# Retrieve Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; books = Book.objects.all(); print(f'Total books: {books.count()}'); [print(f'- {book.id}: {book}') for book in books]"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Total books: 1
- 1: The Pragmatic Programmer by Andrew Hunt (1999)
```
