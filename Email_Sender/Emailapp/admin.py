from django.contrib import admin
from .models import *
# Register your models here.
class users(admin.ModelAdmin):
    list_display = ['id','email','password']
admin.site.register(User,users)

class otp_dis(admin.ModelAdmin):
    list_display = ['id','user','otp_code']
admin.site.register(otp,otp_dis)