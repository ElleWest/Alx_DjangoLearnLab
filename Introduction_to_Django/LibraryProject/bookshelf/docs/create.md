# Create Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; book = Book.objects.create(title='The Pragmatic Programmer', author='Andrew Hunt', publication_year=1999); print(f'Created book: {book.id} | {book}')"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Created book: 1 | The Pragmatic Programmer by Andrew Hunt (1999)
```
