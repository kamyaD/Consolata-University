from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import TblStudentsAdmissions
from .forms import StudentCreationForm
from django.core.mail import send_mass_mail



# Create your views here.
@login_required
def view_admin_panel(request):
    template = 'admin/admin_panel.html'
    students = TblStudentsAdmissions.objects.all()

    form = StudentCreationForm()

    context = {
        'students': students,
        'form': form
    }

    return render(request,template,context)

@login_required
def admit_new_student(request):
    if request.method == 'POST':
        post = request.POST
        student = TblStudentsAdmissions.objects.create(
            image= request.FILES.get('photo'),
            registration_number = post.get('reg-no'),
            first_name = post.get('first-name'),
            last_name = post.get('last-name'),
            nationality = post.get('nationality'),
            id_passport = post.get('id-passport'),
            date_of_birth = post.get('birth-date'),
            contact = post.get('contact'),
            email = post.get('email'),
            occupation = post.get('occupation'),
            address = post.get('address'),
            sponsor = post.get('sponsor'),
            admission_year = post.get('year-of-admission'),
            month = post.get('month-of-admission'),
            responsible = post.get('responsible-name'),
            telephone = post.get('telephone'),
            type_of_sponsorship = post.get('type_of_sponsorship'),
            language_spoken = post.get('spoken-language'),
            language_to_learn = post.get('language-to-learn'),
            course_type = post.get('type-of-course'),
            duration = post.get('duration'),
            start_date = post.get('biggining-date'),
            other_courses = post.get('other-courses'),
            # self = post.get('self'),
            modality= post.get('modality_of_study')

        )

        messages.success(request, "Student record created successfully")
        return redirect('consolata_admin:admin-panel')



@login_required
def view_individual_sudent(request, id):
    template = 'admin/individual_stident.html'
    student = TblStudentsAdmissions.objects.get(studentid=id)
    form = StudentCreationForm()

    context = {
        'student': student,
        'form': form
    }

    return render(request,template,context)

@login_required
def update_student_records(request, id):
    if request.method == 'POST':
        post = request.POST
        student = TblStudentsAdmissions.objects.get(studentid=id)
        
        student.photo = request.FILES.get('photo')
        student.registration_number = post.get('reg-no')
        student.first_name = post.get('first-name')
        student.last_name = post.get('last-name')
        student.nationality = post.get('nationality')
        student.Id_or_passport_no = post.get('id-passport')
        student.date_of_birth = post.get('birth-date')
        student.contact = post.get('contact')
        student.email = post.get('email')
        student.occupation = post.get('occupation')
        student.address = post.get('address')
        student.sponsor = post.get('sponsor')
        student.year_of_admission = post.get('year-of-admission')
        student.month_of_admission = post.get('month-of-admission')
        student.name_of_responsible = post.get('responsible-name')
        student.phone = post.get('telephone')
        student.type_of_sponsorship = post.get('type_of_sponsorship')
        student.language_spoken = post.get('spoken-language')
        student.language_to_learn = post.get('language-to-learn')
        student.type_of_course = post.get('type-of-course')
        student.duration = post.get('duration')
        student.beginning_date = post.get('biggining-date')
        student.other_courses = post.get('other-courses')
        student.self = post.get('self')
        student.modality = post.get('modality_of_study')
        student.save()

        messages.success(request, "Student record updated successfully")
        return redirect('consolata_admin:student-panel', id=student.studentid)
    

@login_required
def get_mailing_list(request):
    template = 'admin/mailing_list.html'
    students = TblStudentsAdmissions.objects.all()
    for student in students:
        student.name = f"{student.first_name} {student.last_name}"

    context = {
        'students': students,
    }

    return render(request,template,context)

@login_required
def send_bulk_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = 'you@example.com'  # or settings.DEFAULT_FROM_EMAIL

        students = TblStudentsAdmissions.objects.exclude(email__isnull=True).exclude(email__exact='').exclude(mail_status='inactive')

        # Prepare the message tuples
        recipient_messages = [
            (subject, message, from_email, [student.email])
            for student in students
        ]

        send_mass_mail(recipient_messages, fail_silently=False)
        messages.success(request, "Bulk emails sent successfully.")
        return redirect('consolata_admin:mailing-list')  # Replace with your actual redirect

    return render(request, 'admin/mailing_list.html')
