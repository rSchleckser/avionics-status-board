from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    bems_id = forms.IntegerField(label="BEMS ID")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "bems_id", "job_title", "role", "location", "shift", "password1", "password2"]
