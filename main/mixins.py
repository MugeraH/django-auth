from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AdminAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return redirect("auth-app:user_page")
        return super().dispatch(request, *args, **kwargs)
    
    
class SuperUserAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an superuser."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_super:
            return redirect("auth-app:superuser_page")
        return super().dispatch(request, *args, **kwargs)
