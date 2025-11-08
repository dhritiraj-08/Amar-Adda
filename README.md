# Amar Adda - Youth Creator Collective Website

Official website for Amar Adda, the flagship youth creator collective of Assam & Northeast India.

## Features

- Modern, responsive design
- Dark/Light mode toggle
- Interactive work showcase with accordion layout
- Team member profiles
- Contact form with email integration
- Service showcase
- Project detail pages

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Fonts**: Bebas Neue, Coolvetica
- **Deployment**: Vercel

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Deployment to Vercel

### Prerequisites
- GitHub account
- Vercel account (sign up at https://vercel.com)

### Steps

1. **Push your code to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

2. **Deploy to Vercel:**
   - Go to https://vercel.com
   - Click "Add New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the Flask app
   - Click "Deploy"

3. **Your site will be live at:**
```
https://your-project-name.vercel.app
```

### Environment Variables (Optional)

If you want to use environment variables for sensitive data:

1. In Vercel dashboard, go to your project
2. Navigate to Settings → Environment Variables
3. Add variables like:
   - `GMAIL_APP_PASSWORD`
   - `SENDER_EMAIL`

Then update `app.py` to use:
```python
import os
sender_password = os.environ.get('GMAIL_APP_PASSWORD')
```

## Project Structure

```
AmarAdda/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── vercel.json                # Vercel configuration
├── .gitignore                 # Git ignore file
├── templates/                 # HTML templates
│   ├── index.html            # Main page
│   ├── project_bark_bark.html
│   ├── project_utopia.html
│   └── project_teencon.html
└── static/                    # Static assets
    ├── style.css             # Main stylesheet
    ├── images/               # Image files
    └── videos/               # Video files
```

## Contact

- **Email**: AmarAdda2004@gmail.com
- **Instagram**: [@amar__adda](https://www.instagram.com/amar__adda)
- **Location**: Lakhimi Nagar, Guwahati, Assam

## License

© 2025 Amar Adda. All rights reserved.
