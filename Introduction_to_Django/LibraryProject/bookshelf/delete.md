# Delete Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; deleted, _ = Book.objects.filter(id=1).delete(); print(f'Deleted rows: {deleted}'); print(f'Remaining count: {Book.objects.count()}')"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Deleted rows: 1
Remaining count: 0
```
