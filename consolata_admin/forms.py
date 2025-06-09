from django import forms
from student.models import TblStudentsAdmission

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = TblStudentsAdmission
        fields = [
            # 'student',  # This is the ForeignKey to CustomUser
            'studentid','first_name','last_name','image', 'nationality','date_of_birth','id_passport','contact','email','occupation','address','admission_year','month','billing_self','organization','responsible',
        'telephone','language_spoken','language_to_learn','course_type','duration','start_date','other_courses','registration_number','modality','mail_status'
        ]
