from django.shortcuts import redirect
from django.http import HttpResponse
# authenticated users cannot access login and sign up pages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blogapp/home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func