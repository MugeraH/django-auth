from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect



def superuser_required(view_func=None, login_url='/login', ):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, 
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser and u.is_authenticated,
        login_url=login_url,
      
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

def adminuser_required(view_func=None, login_url='/login', ):
    """
    Decorator for views that checks that the user is logged in and is a
    admin, 
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin and u.is_authenticated,
        login_url=login_url,
      
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


