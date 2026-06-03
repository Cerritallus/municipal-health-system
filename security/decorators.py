from django.http import HttpResponseForbidden

def role_required(allowed_roles=[]):

    def wrapper(view_func):

        def inner(request, *args, **kwargs):

            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("Access Denied (Role Mismatch)")

            return view_func(request, *args, **kwargs)

        return inner

    return wrapper