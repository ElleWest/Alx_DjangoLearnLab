# Update Operation

**Command:**

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated book title: {book.title}")
```

**Expected Output:**

```
Updated book title: Nineteen Eighty-Four
```
