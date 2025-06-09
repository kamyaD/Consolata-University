from django.shortcuts import render
from student.models import  TblStudentsAdmission

# Create your views here.
def home(request):
    students = TblStudentsAdmission.objects.all()
    print(students.count())

    return render(request, 'home/index.html', {'students': students.count() })