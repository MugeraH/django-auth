from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required,adminuser_required


# from django.contrib.auth.mixins import LoginRequiredMixin

    
def SignupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def LandingPageView(request):
    return render(request,'main/landing.html')


@login_required(login_url='/login')
def HomePageView(request):
    return render(request,'main/home.html')

# @login_required(login_url='/login')
@adminuser_required(login_url='/login',)
def AdminPageView(request):
    if request.user.is_superuser:
        return redirect('auth-app:superuser_page')
        
    if not request.user.is_admin and not request.user.is_superuser:
        return redirect('auth-app:user_page')
    
    return render(request,'main/admin_page.html')

@login_required(login_url='/login')
# @superuser_required(login_url='/login',)
def SuperUserPageView(request):
    if request.user.is_admin:
        return redirect('auth-app:admin_page')
        
    if not request.user.is_admin and not request.user.is_superuser:
        return redirect('auth-app:user_page')
    
    return render(request,'main/super_admin_page.html')

@login_required(login_url='/login')
def UserPageView(request):
    if request.user.is_superuser:
        return redirect('auth-app:superuser_page')
        
    if  request.user.is_admin and not request.user.is_superuser:
        return redirect('auth-app:admin_page')
    
    return render(request,'main/user_page.html')



# class LandingPageView(LoginRequiredMixin,generic.TemplateView):
#     template_name = 'leads/landing_page.html'
