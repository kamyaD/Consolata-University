# student/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages


def student_list(request):
    return HttpResponse("This is the student list page.")
def online_application(request):
    return render(request, 'student/online_application.html', {
    })

def student_login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('student:online-application')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'student/login.html')


