from django import forms
from student.models import TblStudentsAdmissions

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = TblStudentsAdmissions
        fields = [
            # 'student',  # This is the ForeignKey to CustomUser
            'studentid','first_name','last_name','gender','image', 'nationality','date_of_birth','id_passport','contact','email','occupation','address','admission_year','month','billing_self','organization','responsible',
        'telephone','language_spoken','language_to_learn','course_type','duration','start_date','other_courses','registration_number','modality','mail_status', 'marital_status','registration_status', 'school', 'school_of_philosophy','school_of_theology','school_of_counselling', 'anticipated_program_duration', 'ever_studied_at_ciu', 'recomendation_type','disability'
        ]
