from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random
import string


# Create your views here.
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def signup_views(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            return render(request, 'signup.html', {'error': 'Please enter both email and password'})
        
        user = User.objects.create(email = email , password = password)
        
        otp_code = generate_otp()
        otp.objects.create(user = user , otp_code = otp_code)
        
        send_mail(
            'Signup Successfully!!',
            f'Welcome!! Your otp code is {otp_code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        return redirect('otp_verification')
    return render(request, 'signup.html')

def otp_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_code = request.POST.get('otp')
        
        users = User.objects.filter(email = email).first()
        otps = otp.objects.filter(user = users , otp_code = otp_code).first()
        
        if users and otps and not otps.is_experied():
            users.is_verified = True
            users.save()
        else:
            return render(request, 'otp_verification.html',{'error':'InvalidOtpCode'})
            
    return render(request, 'otp_verification.html')


def signin_views(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        users = User.objects.filter(email = email , password = password).first()
        if users:
            return render(request,"index.html")
        else:
            return render(request, 'signin.html',{'error':'InvalidCredentials'})
    return render(request, 'signin.html')

def index_views(request):
    return render(request,"index.html")