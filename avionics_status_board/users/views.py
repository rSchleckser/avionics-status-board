from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser



def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "users/signup.html", {"form": form})


@login_required
def profile_view(request):
    # Fetch user's work assignments (Once Work model is added)
    # user_work = Work.objects.filter(assigned_to=request.user)
    user_work = []  # Placeholder until Work model exists

    context = {
        "user": request.user,
        "user_work": user_work,
    }
    return render(request, "users/profile.html", context)
