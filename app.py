from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'amar-adda-secret-key-2025'

def send_email(name, email, phone, service, message):
    try:
        # Email configuration - UPDATE THESE WITH YOUR GMAIL DETAILS
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "AmarAdda2004@gmail.com"  # Use your Amar Adda Gmail
        sender_password = "lkuiyrlammxjzpbf"   # Gmail App Password (16 digits)
        receiver_email = "AmarAdda2004@gmail.com"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New Query from {name} - {service}"
        
        # Email body
        body = f"""
        New query received from Amar Adda website:
        
        Name: {name}
        Email: {email}
        Phone: {phone if phone else 'Not provided'}
        Service Type: {service}
        
        Message:
        {message}
        
        Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone', '')
        service = request.form.get('service', 'General Inquiry')
        message = request.form.get('message')
        
        # Save to file (backup)
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()},{name},{email},{phone},{service},{message}\n")
        
        # Send email with proper success/error handling
        if send_email(name, email, phone, service, message):
            flash('Message sent successfully! We will get back to you within 24 hours.', 'success')
        else:
            flash('Message received and saved! However, there was an issue with email delivery. We will still get back to you within 24 hours.', 'success')
        
        return redirect('/')
    return render_template('index.html')

@app.route('/project/bark-bark')
def project_bark_bark():
    return render_template('project_bark_bark.html')

@app.route('/project/utopia')
def project_utopia():
    return render_template('project_utopia.html')

@app.route('/project/teencon')
def project_teencon():
    return render_template('project_teencon.html')

if __name__ == '__main__':
    app.run(debug=True)

# For Vercel deployment
app = app
