from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from student.models import TblStudentsAdmissions
from django.contrib import messages
from django.db import IntegrityError

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Account created successfully.")
                return redirect('userauth:login')
            except IntegrityError as e:
                print("IntegrityError:", e)
                if "Duplicate entry" in str(e):
                    form.add_error('first_name', 'Username already exists.')
                else:
                    form.add_error(None, 'Something went wrong. Please try again.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'userauth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            student = TblStudentsAdmissions.objects.filter(email=user.email).first()

            if user.role == 'Student' and student is None:
                login(request, user)
                next_url = request.POST.get('next')
                return redirect(next_url or 'student:online-application')

            else:
                login(request, user)
                next_url = request.POST.get('next')
                return redirect(next_url or 'userauth:profile')
            
            

            # Add more role checks here if needed (e.g., Admin, Staff, etc.)

        return render(request, 'userauth/login.html', {'error': 'Invalid credentials'})

    next_url = request.GET.get('next', '')
    return render(request, 'userauth/login.html', {'next': next_url})



def logout_view(request):
    logout(request)
    return redirect('home:home')

def profile(request):
    form = CustomUserCreationForm()
    return render(request, 'userauth/profile.html', {'form': form})

