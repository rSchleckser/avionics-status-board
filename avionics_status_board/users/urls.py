from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileView, SignupView, ProfileUpdate

app_name = "users"  # Namespace for URL resolution

urlpatterns = [
    # User profile page
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdate.as_view(), name="profile-edit"),

    # Authentication URLs
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
