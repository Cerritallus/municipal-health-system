from django.shortcuts import redirect


def root_redirect(request):

    if not request.user.is_authenticated:
        return redirect("/accounts/login/")

    user = request.user

    # Role-based routing
    if user.role in ["DOCTOR", "ADMIN"]:
        return redirect("/dashboard/")

    if user.role == "NURSE":
        return redirect("/patients/")

    # fallback safety
    return redirect("/accounts/login/")