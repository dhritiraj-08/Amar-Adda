# Email Setup Guide for Amar Adda Contact Form

## Current Status
❌ **Email sending is NOT configured yet**
✅ **Form data is saved to messages.txt as backup**

## To Enable Email Sending:

### Step 1: Update app.py
Open `app.py` and replace these lines (around line 15-16):

```python
sender_email = "your-gmail@gmail.com"  # Replace with your Gmail
sender_password = "your-app-password"   # Replace with your Gmail App Password
```

With your actual Gmail credentials:

```python
sender_email = "yourgmail@gmail.com"        # Your Gmail address
sender_password = "your-16-digit-app-password"  # Gmail App Password (not regular password)
```

### Step 2: Create Gmail App Password
1. Go to your Google Account settings
2. Enable 2-Factor Authentication if not already enabled
3. Go to Security → 2-Step Verification → App passwords
4. Generate a new app password for "Mail"
5. Use this 16-digit password in the code (not your regular Gmail password)

### Step 3: Install Required Package
Run this command in your terminal:
```bash
pip install secure-smtplib
```

## How It Works:
1. **User fills form** on website
2. **Data is saved** to messages.txt (backup)
3. **Email is sent** to AmarAdda2004@gmail.com with:
   - User's name and contact info
   - Service type they selected
   - Their message/query
   - Timestamp

## Email Format:
```
Subject: New Query from [Name] - [Service Type]

New query received from Amar Adda website:

Name: John Doe
Email: john@example.com
Phone: +91 9876543210
Service Type: Event Management

Message:
Hi, I need help organizing a corporate event...

Submitted on: 2025-01-07 15:30:45
```

## Security Notes:
- Never commit your actual Gmail password to code
- Use Gmail App Passwords, not regular passwords
- Keep your credentials secure

## Testing:
Once configured, test by:
1. Filling out the contact form
2. Checking if email arrives at AmarAdda2004@gmail.com
3. Verifying success message appears on website