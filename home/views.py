from django.shortcuts import render
from student.models import TblStudentsAdmissions



# Create your views here.
def home(request):
    students = TblStudentsAdmissions.objects.all()
    print(students.count())

    return render(request, 'home/index.html', {'students': students.count() })