from django.shortcuts import render
from student.models import TblStudentsAdmissions



# Create your views here.
def home(request):
    students = TblStudentsAdmissions.objects.all()
    print(students.count())

    return render(request, 'home/index.html', {'students': students.count() })

def psychology_school(request):
    return render(request, 'home/psychology_school.html')

def theology_school(request):
    return render(request, 'home/theology_school.html')

def philosophy_school(request):
    return render(request, 'home/philosophy_school.html')

def language_center(request):
    return render(request, 'home/language_center.html')