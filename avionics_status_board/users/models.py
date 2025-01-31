from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('lead', 'Lead'),
        ('avionics', 'Avionics Tech'),
    ]

    bems_id = models.IntegerField(unique=True)
    job_title = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='avionics')
    location = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    shift = models.IntegerField()
    
    def is_lead(self):
        return self.role == 'lead'
