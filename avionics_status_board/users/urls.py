from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User profile/home page (should be more specific than "")
    
    path("profile/", views.profile_view, name="profile"),

    # Authentication URLs
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("signup/", views.signup_view, name="signup"),
]
