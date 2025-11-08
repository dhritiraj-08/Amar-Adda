# Gmail Setup for Amar Adda Contact Form

## 🚀 Quick Setup Steps

### Step 1: Enable Gmail App Password
1. **Go to Gmail** and sign in to AmarAdda2004@gmail.com
2. **Click your profile picture** → "Manage your Google Account"
3. **Go to Security tab** on the left
4. **Enable 2-Step Verification** if not already enabled:
   - Click "2-Step Verification"
   - Follow the setup process (use your phone number)
5. **Create App Password**:
   - Still in Security, scroll down to "2-Step Verification"
   - Click "App passwords"
   - Select "Mail" and "Windows Computer"
   - Click "Generate"
   - **Copy the 16-digit password** (like: abcd efgh ijkl mnop)

### Step 2: Update Your Code
1. **Open `app.py`**
2. **Find line 13** that says:
   ```python
   sender_password = "PUT_YOUR_APP_PASSWORD_HERE"
   ```
3. **Replace it with**:
   ```python
   sender_password = "your-16-digit-password-here"
   ```
   (Use the password from Step 1, without spaces)

### Step 3: Test the Setup
1. **Restart your Flask app**:
   ```bash
   python app.py
   ```
2. **Go to your website** and fill out the contact form
3. **Check AmarAdda2004@gmail.com** for the email
4. **Look for success message** on the website

## 📧 What the Email Will Look Like:

**Subject:** New Query from John Doe - Event Management

**Body:**
```
New query received from Amar Adda website:

Name: John Doe
Email: john@example.com
Phone: +91 9876543210
Service Type: Event Management

Message:
Hi, I need help organizing a corporate event for 200 people...

Submitted on: 2025-01-07 15:30:45
```

## 🔧 If You Get Errors:

### "Authentication failed"
- Double-check the 16-digit app password
- Make sure 2-Step Verification is enabled
- Try generating a new app password

### "Connection refused"
- Check your internet connection
- Gmail might be temporarily down

### Still not working?
- All form data is still saved to `messages.txt`
- You can manually check that file for submissions
- Contact me for help debugging

## 🔒 Security Notes:
- **Never share** your app password
- **Don't commit** the password to GitHub
- **Use app passwords**, not your regular Gmail password
- The app password only works for this specific application

## ✅ Once Working:
- Every form submission will email you instantly
- You'll get organized emails with all user details
- Backup copy still saved to messages.txt
- Users see success/error messages on website