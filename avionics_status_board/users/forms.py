from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    bems_id = forms.IntegerField(label="BEMS ID")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "bems_id", "job_title", "role", "location", "shift", "password1", "password2"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "location", "email", "profile_pic", "job_title", "shift"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "ui input"}),
            "last_name": forms.TextInput(attrs={"class": "ui input"}),
            "location": forms.TextInput(attrs={"class": "ui input"}),
            "email": forms.EmailInput(attrs={"class": "ui input"}),
            "profile_pic": forms.FileInput(attrs={"class": "ui input"}),
            "job_title": forms.TextInput(attrs={"class": "ui input"}),
            "shift": forms.NumberInput(attrs={"class": "ui input"}),
        }
