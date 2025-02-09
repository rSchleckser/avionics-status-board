from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, ProfileUpdateForm 
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from work.models import Work

class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("home")  # Redirect after successful signup

    def form_valid(self, form):
        """Logs the user in after successful signup."""
        response = super().form_valid(form)
        login(self.request, self.object)  # Auto-login user
        return response


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_work"] = Work.objects.filter(assigned_to=self.request.user).order_by("-assigned_at")  
        return context


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        """Ensure the user can only edit their own profile."""
        return self.request.user

    def test_func(self):
        """Check if the user is updating their own profile."""
        return self.get_object() == self.request.user
