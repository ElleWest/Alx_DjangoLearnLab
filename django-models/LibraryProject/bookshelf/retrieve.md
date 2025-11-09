# Retrieve Operation

Command

```
./venv/bin/python manage.py shell -c "from bookshelf.models import Book; book = Book.objects.get(id=1); print(f'Book: {book.title}, Author: {book.author}, Year: {book.publication_year}')"
```

Output

```
7 objects imported automatically (use -v 2 for details).

Book: 1984, Author: George Orwell, Year: 1949
```
