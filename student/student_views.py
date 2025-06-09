from django.shortcuts import render
from .forms import StudentCreationForm

# Create your views here.

def online_application(request):
    template = 'student/online-application.html'
    
    form = StudentCreationForm()
    context = {
        'form': form,
        
    }

    return render(request,template,context)