from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return self.request.user  # Fetch the logged-in user's profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_work"] = Work.objects.filter(assigned_to=self.request.user)  # ✅ Corrected field
        return context