from django.db import models
from website.models import *

# Create your models here.
class StripeAccountKey(models.Model):
    stripe_public_key = models.CharField(max_length=5000)
    stripe_secret_key = models.CharField(max_length=5000)

    class Meta:

        verbose_name = 'Stripe Account Key'
        verbose_name_plural = 'Stripe Account Key'


class StudentRegistration(models.Model):
    STATUS_CHOICES = (
        (1, 'Unpaid'),
        (2, 'Paid'),
    )
    COURSE_TYPE = (
        (1, 'Auto'),
        (2, 'Manual'),
    )
    PREFIX_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),
    )
    PREVIOUS_EXPERIENCE_CHOICES = (
        (1, 'I had no lessons and i am not confident'),
        (2, 'I had no lessons but i am confident'),
        (3, 'I had 1-9 hours of driving lessons'),
        (4, 'I had 10-14 hours of driving lessons'),
        (5, 'I had 15-19 hours of driving lessons'),
        (6, 'I had 20-24 hours of driving lessons'),
        (7, 'I had 30 hours of driving lessons'),
        (8, 'I can drive at test standards, I want to retake'),
    )
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    registration_id = models.CharField(max_length=500)
    name_prefix = models.CharField(max_length=150, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    driving_license_number = models.CharField(max_length=18, null=True, blank=True)
    learning_difficulty = models.BooleanField(default=False)
    fast_track_test = models.BooleanField(default=False)
    start_date = models.DateField()
    course_type = models.IntegerField(choices=COURSE_TYPE)
    previous_experience = models.IntegerField(choices=PREVIOUS_EXPERIENCE_CHOICES)
    address = models.CharField(max_length=550)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    total_initial_deposit = models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)
    

    class Meta:

        verbose_name = 'Student Registration'
        verbose_name_plural = 'Student Registrations'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
class StudentRegistrationCourse(models.Model):
    registration = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name="related_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Student Registration Course'
        verbose_name_plural = 'Student Registration Courses'

    def __str__(self):
        return self.course.name


