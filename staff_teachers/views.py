from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TblTeachersPay, TblSchoolInvoice, TblRecordSlip,Timetable, studentsResults
from student.models import StudentClassSignIN
from .forms import TimetableForm
import datetime
import csv
import io


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

    context = {
        'school_invoices': school_invoices,
        'record_slips': record_slips
    }

    return render(request,template,context)



def create_timetable(request):
    if request.method == 'POST':
        post = request.POST

        timetable = Timetable.objects.create(
            day=post.get('day'),
            class_no=post.get('class'),
            from_time=post.get('from_time'),
            to_time=post.get('to_time'),
            lecturer=post.get('lecturer'),
            courses=post.get('courses'),
            room=post.get('room')
        )

        messages.success(request, "Student record created successfully")
        return redirect('staff_teachers:timetable')
    else:
        template = 'staff/timetable.html'

        # Get today's day name (e.g. 'Monday')
        today = datetime.datetime.today().strftime('%A')


        # Only fetch records for today if it's a weekday
        if today in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            tables = Timetable.objects.filter(day=today)
        
        else:
            tables = Timetable.objects.all()  # Return empty QuerySet for weekends

        form = TimetableForm()

        return render(request, template, {'tables': tables, 'form':form})

    
def edit_time_table(request, id=None):
    print("id", id)
    if request.method == 'POST':
        table = Timetable.objects.get(pk=id)
        post = request.POST
        table.day = post.get('day')
        table.class_no = post.get('class')
        table.from_time = post.get('from_time')
        table.to_time = post.get('to_time')
        table.lecturer = post.get('lecturer')
        table.courses = post.get('courses')
        table.room = post.get('room')
        table.save()
        messages.success(request,"Time table updated Successfully")

        return redirect('staff_teachers:timetable')
    
    template='staff/edit_timetable.html',
    table = Timetable.objects.get(pk=id)
    form = TimetableForm()
    context = {'table': table, 'form': form}

    return render(request, template, context)

def delete_timetable_raw(request, id):
    table = table = Timetable.objects.get(pk=id)
    table.delete()
    return redirect('staff_teachers:timetable')

def fetch_student_class_sign(request):
    template = 'staff/class_sign.html'
    signs = StudentClassSignIN.objects.all()

    context = {
        'signs': signs
    }
    return render(request, template, context)
    

    
def normalize_header(header):
    return header.lower().strip().replace(" ", "_")

def upload_results_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            messages.error(request, "Please upload a valid CSV file.")
            return render(request, 'upload_predictions.html')

        try:
            decoded_file = csv_file.read().decode('utf-8-sig')  # handles BOM
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            print("reader===>", reader)

            headers = [normalize_header(h) for h in next(reader)]
            reader = csv.DictReader(io_string, fieldnames=headers)

            saved_rows = 0
            skipped_rows = 0
            
            pass

            for row in reader:

                try:
                    

                    studentsResults.objects.create(
                        congregation=row.get('cong', '').strip(),
                        s_no=row.get('s/no', '').strip(),
                        reg_no=row.get('reg.no', '').strip(),
                        name=row.get('student_name', '').strip(),
                        plato_republic=row.get('plato_republic', '').strip(),
                        modern_world_history = row.get('modern_world_history', '').strip(),
                        special_ethicks=row.get('special_ethics', '').strip(),
                        logic = row.get('logic', '').strip(),
                        emmanuel_kant = row.get('philosophy_of_emmanuel_kant', '').strip(),
                        edith_stein = row.get('edith_stein_phenomenology', '').strip(),
                        philosophical_latin = row.get('philosophical_latin', '').strip(),
                        christianity_philosophy = row.get('christianity_&_philosophy', '').strip(),
                        ancient_thought = row.get('philosophy_&_know_the_ancient_thought', '').strip(),
                        comprehensive_written = row.get('comprehensives_written', '').strip(),
                        comprehensives_oral = row.get('comprehensives_orals', '').strip(),
                    )
                    saved_rows += 1

                except Exception as e:
                    skipped_rows += 1
                    print(f"Skipping row due to error: {e}")

            messages.success(request, f"Upload complete: {saved_rows} saved, {skipped_rows} skipped.")

        except Exception as e:
            messages.error(request, f"Error processing CSV file: {e}")

    return redirect('staff_teachers:results')

def show_exam_results(request):
    template = 'staff/show_results.html'
    results = studentsResults.objects.all()
    
    context = {
        'results': results
    }

    return render(request, template, context)



