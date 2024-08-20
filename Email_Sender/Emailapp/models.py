from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email
    
class otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_experied(self):
        return(timezone.now() - self.created_at) > 300

