#!/usr/bin/env python3
"""
Test script to verify Gmail setup for Amar Adda contact form
Run this after setting up your Gmail App Password
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def test_email_setup():
    try:
        print("🧪 Testing Gmail setup for Amar Adda...")
        
        # Email configuration - SAME AS IN app.py
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "AmarAdda2004@gmail.com"
        sender_password = "PUT_YOUR_APP_PASSWORD_HERE"  # UPDATE THIS
        receiver_email = "AmarAdda2004@gmail.com"
        
        # Create test message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "🧪 Test Email - Amar Adda Contact Form Setup"
        
        body = f"""
        This is a test email to verify your Amar Adda contact form setup.
        
        If you receive this email, your Gmail configuration is working correctly!
        
        Test sent on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Next steps:
        1. Update app.py with the same password
        2. Restart your Flask app
        3. Test the contact form on your website
        
        - Amar Adda Website Team
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        print("📧 Connecting to Gmail...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        print("🔐 Logging in...")
        server.login(sender_email, sender_password)
        
        print("📤 Sending test email...")
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        print("✅ SUCCESS! Test email sent successfully!")
        print("📬 Check your AmarAdda2004@gmail.com inbox")
        print("🚀 Your contact form is ready to use!")
        
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ AUTHENTICATION ERROR!")
        print("🔧 Check your Gmail App Password")
        print("📋 Make sure 2-Step Verification is enabled")
        return False
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("🔧 Check your internet connection and Gmail settings")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🎬 AMAR ADDA - EMAIL SETUP TEST")
    print("=" * 50)
    
    # Check if password is updated
    if "PUT_YOUR_APP_PASSWORD_HERE" in open(__file__).read():
        print("⚠️  Please update the sender_password in this file first!")
        print("📝 Replace 'PUT_YOUR_APP_PASSWORD_HERE' with your 16-digit Gmail App Password")
    else:
        test_email_setup()
    
    print("=" * 50)