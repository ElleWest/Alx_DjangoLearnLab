# Create Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949); print(f'Created book: {book.id} | {book}')"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Created book: 1 | 1984 by George Orwell (1949)
```
