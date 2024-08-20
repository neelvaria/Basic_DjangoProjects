from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('signup/',views.signup_views,name="signup"),
    path('signin/',views.signin_views,name="signin"),
    path('otp_verification/',views.otp_verification,name="otp_verification"),
    path('index/',views.index_views,name="index"),
]