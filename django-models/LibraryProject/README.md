# LibraryProject

This is the `LibraryProject` Django project used for the Introduction to Django exercise.

Run the development server after creating a virtual environment and installing dependencies from `requirements.txt`.

Basic steps:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd Introduction_to_Django/LibraryProject
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the Django welcome page.
