from datetime import date
from dateutil.relativedelta import relativedelta
from django import forms
from website.models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm



def initial_date():
    return date.today() + relativedelta(months=+3)



class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'


class CourseCategoryForm(forms.ModelForm):

    class Meta:

        model = CourseCategory
        fields = '__all__'



class CourseForm(forms.ModelForm):

    class Meta:

        model = Course
        fields = '__all__'



class StripeAccountKeyForm(forms.ModelForm):

    class Meta:

        model = StripeAccountKey
        fields = '__all__'


class StudentRegistrationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=initial_date)

    class Meta:

        model = StudentRegistration
        fields = ('name_prefix', 'first_name', 'last_name', 'dob', 'phone', 'email', 'driving_license_number',
                    'start_date', 'previous_experience', 'address', 'city', 'state', 'zip_code', 'course_type')
        widgets = {
            'dob' : DateInput(),
            'start_date' : DateInput(),
        }
        labels = {
            'dob' : 'Date of Birth'
        }
