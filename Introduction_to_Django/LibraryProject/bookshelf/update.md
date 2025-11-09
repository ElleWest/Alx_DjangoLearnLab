# Update Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; book = Book.objects.get(id=1); book.title = 'Nineteen Eighty-Four'; book.save(); updated_book = Book.objects.get(id=1); print(f'Updated book title: {updated_book.title}')"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Updated book title: Nineteen Eighty-Four
```
