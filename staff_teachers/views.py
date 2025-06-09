from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TblTeachersPay, TblSchoolInvoice, TblRecordSlip

# Create your views here.
@login_required
def view_teachers_pay(request):
    template = 'staff/pay_update.html'
    teachers = TblTeachersPay.objects.all()

    for teacher in teachers:
        teacher.name = f"{teacher.first_name} {teacher.last_name}" 

    # form = StudentCreationForm()

    context = {
        'teachers': teachers,
        # 'form': form
    }

    return render(request,template,context)

@login_required
def admin_office(request):
    template = 'staff/admin_office.html'
    school_invoices = TblSchoolInvoice.objects.all()
    record_slips = TblRecordSlip.objects.all()


    # for invoice in school_invoices:
    #     invoice.name = f"{invoice.first_name} {invoice.last_name}" 

    # form = StudentCreationForm()

    context = {
        'school_invoices': school_invoices,
        'record_slips': record_slips
    }

    return render(request,template,context)


