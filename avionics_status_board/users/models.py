from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('lead', 'Lead'),
        ('avionics', 'Avionics Tech'),
    ]

    bems_id = models.PositiveIntegerField(unique=True)
    job_title = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='avionics')
    location = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    shift = models.PositiveIntegerField(default=1)  # Assuming 1 is a default shift

    def is_lead(self):
        return self.role == 'lead'

    @property
    def is_technician(self):
        return self.role == 'avionics'

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser

    def __str__(self):
        return self.username
