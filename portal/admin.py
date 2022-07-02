from django.contrib import admin
from .models import *

# Register your models here.
# class StudentRegistrationCourseInline(admin.TabularInline):
#     model = StudentRegistrationCourse
    
# @admin.register(StudentRegistration)
# class StudentRegistrationAdmin(admin.ModelAdmin):

#     list_display = ('first_name', 'last_name', 'email', 'total_initial_deposit')
#     inlines = [StudentRegistrationCourseInline]