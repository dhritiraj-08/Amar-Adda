# Django Setup Guide for Amar Adda

## Your project has been converted from Flask to Django!

All functionality remains the same - the website looks and works exactly as before.

## What Changed:

### Backend Framework
- **Before**: Flask
- **After**: Django

### Key Benefits of Django:
1. Built-in admin panel to view contact form submissions
2. Better ORM for database management
3. More scalable for future features
4. Better security features out of the box

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations (Create Database)
```bash
python manage.py migrate
```

### 3. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 4. Run the Server
```bash
python manage.py runserver
```

### 5. Access Your Site
- **Website**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin

## Admin Panel Features

The admin panel allows you to:
- View all contact form submissions
- Filter by service type and date
- Search through messages
- Export data

## File Structure Changes

### New Files:
- `manage.py` - Django management command
- `amaradda/` - Project configuration folder
  - `settings.py` - All project settings
  - `urls.py` - Main URL routing
  - `wsgi.py` - WSGI application
- `website/` - Main app folder
  - `models.py` - Database models
  - `views.py` - View functions (replaces Flask routes)
  - `urls.py` - App URL routing
  - `admin.py` - Admin panel configuration

### Removed Files:
- `app.py` (replaced by Django structure)

### Template Changes:
- `{{ url_for() }}` → `{% url %}` and `{% static %}`
- `get_flashed_messages()` → Django messages framework

## Environment Variables (Production)

For production deployment, set these in Vercel:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.vercel.app
EMAIL_HOST_USER=AmarAdda2004@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Database

- **Development**: SQLite (db.sqlite3)
- **Production**: Can use PostgreSQL, MySQL, or any Django-supported database

## Deployment to Vercel

The project is ready for Vercel deployment:

1. Push to GitHub
2. Import to Vercel
3. Vercel will automatically detect Django
4. Add environment variables in Vercel dashboard
5. Deploy!

## Testing

Everything should work exactly as before:
- ✅ Home page with all sections
- ✅ Contact form with email sending
- ✅ Dark/Light mode toggle
- ✅ Work section with accordion
- ✅ Project detail pages
- ✅ All styling intact

## Need Help?

- Django Documentation: https://docs.djangoproject.com/
- Django Tutorial: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

## Notes

- The website looks and functions exactly the same
- All your CSS and JavaScript remain unchanged
- Email functionality works the same way
- Contact form submissions are now also saved to database
- You can view submissions in the admin panel
