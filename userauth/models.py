from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        # ('Admin', 'Admin'),
        ('Student', 'Student'),
        ('Lecturer', 'Lecturer'),
        ('Formator', 'Formator'),
        ('Registrar', 'Registrar'),
        ('Admin', 'Admin')
    )
    DEPARTMENT_CHOICES = (
        ('Philosophy', 'Philosophy'),   
        ('Language', 'Language'),
        ('Psychology', 'Psychology'),
    )
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    MARITAL_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Priest','Priest'),
        ('Sister', 'Sister')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True)
    is_active = models.BooleanField(default=False)
    school = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=True)
    # school = models.CharField(max_length=250, blank=True, null=True)
    
    

    
    def __str__(self):
        return self.username
