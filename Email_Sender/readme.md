## How run a Project

**Clone this Repositary**
https://github.com/neelvaria/Django_Emailsender.git


### Steps for Scratch!!!
#### Step 1.
```
pip install virtualenv
python -m venv (env_name)

#once you make env then you need to activate it
<virtual_env_name>\Scripts\activate
``` 

#### Step 2.
```
django-admin startproject myproject_name .
cd myproject
``` 

#### Step 3.
```
python manage.py startapp startapp_name
```

#### Step 4.  Add your app to INSTALLED_APPS in settings.py
```
INSTALLED_APPS = [
    # other apps
    'projectapp_name',
]
```
#### Step 5. Configure Email Settings
1. Create a Gmail account
2. Enable 2-Factor Authentication:
   Go to My [Google Account](https://myaccount.google.com) .
3. Create a App password <br><br>
Go to My [Google Account](https://myaccount.google.com) .<br>
--> Search for "App Password" <br>
--> Create an "App Password". These are easy to delete and recreate, do this as needed. <br>
--> Copy the App Password for your Django project's environment variables. Such as. a dotenv file .env or in your production systems environment variables (over time you should upgrade to a domain you own with a production-ready transactional email service)

**4. Add this into the SETTINGS.py**
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```
#### Step 6. Create Models In userauth/models.py, define your custom models for user and OTP:

#### Step 7. Create Views for Signup and OTP Verification
##### In userauth/views.py, create views for handling signup, sending email, and OTP verification:

#### Step 8. Create Templates: 
**Add this in Settings.py** 
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        
        #Exist Code
    }
]
```

#### Create templates folder in App & add all templates.

#### Step 8: Configure URLs 
--> **In app_name/urls.py, configure the URLs for your views:**
```
from django.urls import path
from . import views

urlpatterns = [
    path('viewname/', views.views_functionapp, name=''),
]
```

--> **Include these URLs in your project's urls.py:**
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appname.urls')),
]
```

#### Step 9. Migrate Database
```
python manage.py makemigrations
python manage.py migrate
```

#### Step 10. Testing your Application
```
python manage.py runserver
```

#### Step 11. Create SuperUser for Database:
```
py manage.py createsuperuser
```

**[Linkedin](https://www.linkedin.com/in/neelvaria/)**<br>
**[Instagram](https://www.instagram.com/neelvariaa/)**