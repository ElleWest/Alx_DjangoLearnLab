# Update Operation

Command

```
# Update Operation

Command
```

./venv/bin/python manage.py shell -c "from bookshelf.models import Book; book = Book.objects.get(id=1); book.title = 'Nineteen Eighty-Four'; book.save(); print(f'Updated book: {book.id} | {book}')"

```

Output
```

7 objects imported automatically (use -v 2 for details).

Updated book: 1 | Nineteen Eighty-Four by George Orwell (1949)

```

```

Output

```
7 objects imported automatically (use -v 2 for details).

Updated book: 1 | The Pragmatic Programmer by Andrew Hunt (2019)
```
