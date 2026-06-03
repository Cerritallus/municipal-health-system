from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_view(request):

    if request.user.is_authenticated:
        return redirect_based_on_role(request.user)

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect_based_on_role(user)

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


def redirect_based_on_role(user):

    if user.role in ["DOCTOR", "ADMIN"]:
        return redirect("/dashboard/")

    elif user.role == "NURSE":
        return redirect("/patients/")

    return redirect("/accounts/login/")

def register_view(request):

    if request.user.is_authenticated:
        return redirect_based_on_role(request.user)
    
    if request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)

            return redirect("/dashboard/")

    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

def logout_view(request):

    if request.method == "POST":
        logout(request)
        return redirect("/accounts/login/")

    return redirect("/accounts/login/")