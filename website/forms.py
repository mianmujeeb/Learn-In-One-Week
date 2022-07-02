from django import forms
from .models import *


class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'


class InstructorForm(forms.ModelForm):

    class Meta:

        model = Instructor
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'license_number', 'issue_date', 'years_of_experience', 
                    'adi_number', 'adi_expiry_date', 'grade', 'transmission', 'car_make', 'car_brand', 'car_model', 'address', 
                    'city', 'state', 'zip_code', 'country', 'image')
        widgets = {
            'adi_expiry_date' : DateInput(),
            'issue_date' : DateInput(),
        }
        labels = {
            'adi_number' : 'ADI Number',
            'adi_expiry_date' : 'ADI Expiry Date',
        }
