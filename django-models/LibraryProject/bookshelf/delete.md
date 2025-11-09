# Delete Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; book = Book.objects.get(id=1); book.delete(); remaining_books = Book.objects.all(); print(f'Deletion confirmed. Remaining books: {remaining_books.count()}')"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Deletion confirmed. Remaining books: 0
```
