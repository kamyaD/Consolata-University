from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'userauth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url or 'student:online-application')  
        else:
             return render(request, 'userauth/login.html', {'error': 'Invalid credentials'})
    
    next_url = request.GET.get('next', '')
    return render(request, 'userauth/login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    form = CustomUserCreationForm()
    return render(request, 'userauth/profile.html', {'form': form})

