import random
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import User

def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_email_otp(email):
    otp = generate_otp()
    try:
        user, created = User.objects.get_or_create(email=email)
        user.email_otp = otp
        user.is_email_verified = False
        user.save()

        # Send OTP via email
        send_mail(
            subject="Your Email OTP Verification Code",
            message=f"Your OTP is: {otp}",
            from_email="tayeyohanis8@gmail.com",  # Change to your app's email
            recipient_list=[email],
        )
        return True
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return False

def send_developer_status_email(developer):
    """
    Send email notification about developer account status
    """
    subject = f"Developer Account Status Update - {developer.status.title()}"
    
    # Render the HTML email template
    html_message = render_to_string('users/developer_status_email.html', {
        'developer': developer
    })
    
    # Send the email
    try:
        send_mail(
            subject=subject,
            message='',  # Plain text version (empty as we're using HTML)
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[developer.user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending developer status email: {e}")
        return False

def send_welcome_email(user):
    """
    Send welcome email to new user
    """
    subject = "Welcome to Government App Store!"
    
    # Render the HTML email template
    html_message = render_to_string('users/welcome_email.html', {
        'user': user
    })
    
    # Send the email
    try:
        send_mail(
            subject=subject,
            message='',  # Plain text version (empty as we're using HTML)
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending welcome email: {e}")
        return False
