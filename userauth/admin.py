from django.contrib import admin

# Register your models here.
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'school', 'role', 'is_active')
    list_display = ('first_name', 'last_name', 'school','role', 'is_active')
admin.site.register(CustomUser,CustomUserAdmin)

