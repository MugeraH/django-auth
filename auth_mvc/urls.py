from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import(
    LoginView,
    LogoutView,    
    )
from main.views import SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('signup/',SignupView,name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
]
