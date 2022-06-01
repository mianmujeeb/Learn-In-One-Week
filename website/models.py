from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    class Meta:

        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'
        
        
class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    class Meta:

        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return self.name


class GeneralInfo(models.Model):
    title = models.CharField(max_length=100)
    favicon = models.ImageField(upload_to='Favicons/')
    logo = models.ImageField(upload_to='Logo/')

    class Meta:
        verbose_name = 'General Info'
        verbose_name_plural = 'General Info'
        
        

class About(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    detail = RichTextField()
    image = models.ImageField(upload_to='About')

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='Service')

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name



class CourseCategory(models.Model):
    STAUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(choices=STAUS_CHOICES, default=1)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    class Meta:

        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'

    def __str__(self):
        return self.name




class Course(models.Model):
    STAUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(choices=STAUS_CHOICES, default=1)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    hours = models.IntegerField()
    price_auto = models.DecimalField(max_digits=999, decimal_places=2)
    price_manual = models.DecimalField(max_digits=999, decimal_places=2)
    advance_deposit = models.DecimalField(max_digits=999, decimal_places=2)
    description =  RichTextField()

    class Meta:

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name 



class Testimonial(models.Model):
    client_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150, null=True, blank=True)
    review = models.TextField()
    image = models.ImageField(upload_to='Testimonials/', null=True, blank=True)
    

    class Meta:

        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.client_name



class CoverageArea(models.Model):
    STAUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(choices=STAUS_CHOICES, default=1)
    name = models.CharField(max_length=150)
    
    class Meta:

        verbose_name = 'Coverage Area'
        verbose_name_plural = 'Coverage Areas'

    def __str__(self):
        return self.name



class CoverageAreaCity(models.Model):
    coverage_area = models.ForeignKey(CoverageArea, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=200)

    class Meta:

        verbose_name = 'Coverage Area City'
        verbose_name_plural = 'Coverage Area Citiess'

    def __str__(self):
        return self.name



class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    class Meta:

        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question



class WhyUs(models.Model):
    STAUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(choices=STAUS_CHOICES, default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:

        verbose_name = 'Why Us'
        verbose_name_plural = 'Why Us'

    def __str__(self):
        return self.title



class Stats(models.Model):
    years_of_operation = models.IntegerField()
    students = models.IntegerField()
    instructors = models.IntegerField()

    class Meta:

        verbose_name = 'Stats'
        verbose_name_plural = 'Stats'




class Instructor(models.Model):
    GRADE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('6', '6'),
        ('5', '5'),
        ('4', '4'),
    )
    TRANSMISSION_CHOICES = (
        (1, 'Manual'),
        (2, 'Automatic'),
    )
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    email = models.EmailField()
    license_number = models.CharField(max_length=150)
    years_of_experience = models.IntegerField()
    adi_number = models.CharField(max_length=250)
    adi_expiry_date = models.DateField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    transmission = models.IntegerField(choices=TRANSMISSION_CHOICES)
    car_make = models.CharField(max_length=150)
    car_brand = models.CharField(max_length=150)
    car_model = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Instructors')

    class Meta:

        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return self.name
    
    

