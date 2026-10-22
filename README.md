# Meme Buddy

Meme Buddy is a Django web app for sharing and browsing memes. Users can register, sign in, upload posts with captions and categories, save drafts, publish posts, and manage their posts. The app also includes post detail pages and password-reset flows by email.

## Tech stack

- Python
- Django
- PostgreSQL
- Pillow for image uploads

## Getting started

### Requirements

- Python
- A PostgreSQL database
- SMTP credentials for password-reset emails

### Install and run

From the repository root, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Django Pillow dj-database-url psycopg2-binary
```

Configure the database and email settings for your environment in `django_pro/django_pro/settings.py`. Do not commit passwords, secret keys, or other credentials.

Then initialize and run the app:

```powershell
cd django_pro
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. Sign in to the Django admin at <http://127.0.0.1:8000/admin/> and add categories before creating posts.

## Main routes

| Route | Description |
| --- | --- |
| `/` | Browse published posts |
| `/about/` | About page |
| `/register/` | Create an account |
| `/login/` | Sign in |
| `/new_post/` | Create a post |
| `/dash/` | View your posts and drafts |
| `/admin/` | Django administration |

## Project layout

```text
django_pro/
├── django_pro/   # Django project settings and URL configuration
├── instagram/    # App models, views, forms, templates, and static files
├── media/        # Uploaded post images
└── manage.py     # Django management entry point
```
