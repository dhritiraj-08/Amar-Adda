from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from .models import ContactMessage


def send_contact_email(name, email, phone, service, message):
    """Send email notification for contact form submission"""
    try:
        subject = f"New Query from {name} - {service}"
        
        email_body = f"""
New query received from Amar Adda website:

Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Service Type: {service}

Message:
{message}

Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        send_mail(
            subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def home(request):
    """Home page view with contact form"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        service = request.POST.get('service', 'General Inquiry')
        message_text = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            message=message_text
        )
        
        # Save to file (backup)
        try:
            with open('messages.txt', 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now()},{name},{email},{phone},{service},{message_text}\n")
        except Exception as e:
            print(f"Error writing to file: {e}")
        
        # Send email
        if send_contact_email(name, email, phone, service, message_text):
            messages.success(request, 'Message sent successfully! We will get back to you within 24 hours.')
        else:
            messages.success(request, 'Message received and saved! However, there was an issue with email delivery. We will still get back to you within 24 hours.')
        
        return redirect('home')
    
    return render(request, 'index.html')


def project_bark_bark(request):
    """Bark Bark project detail page"""
    return render(request, 'project_bark_bark.html')


def project_utopia(request):
    """Utopia project detail page"""
    return render(request, 'project_utopia.html')


def project_teencon(request):
    """Teencon project detail page"""
    return render(request, 'project_teencon.html')
