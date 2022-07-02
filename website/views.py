from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from website.models import *
from website.forms import *
from portal.forms import *

import stripe

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    general_info = GeneralInfo.objects.first()
    courses_categories = CourseCategory.objects.all()
    social_links = SocialLink.objects.all()
    about_us = About.objects.first()
    contact = ContactInfo.objects.first()
    why_us = WhyUs.objects.all()
    testimonials = Testimonial.objects.all()
    benifits = Benifit.objects.all()
    
    
    context = {
        'i' : general_info,
        'j' : courses_categories,
        'social_links' : social_links,
        'testimonials' : testimonials,
        'about' : about_us,
        'why_us' : why_us,
        'contact' : contact,
        'benifits' : benifits,
    }
    return render(request, 'website/index.html', context)


def reviews(request):
    general_info = GeneralInfo.objects.first()
    courses_categories = CourseCategory.objects.all()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    reviews = Testimonial.objects.all()
    
    context = {
        'i' : general_info,
        'j' : courses_categories,
        'social_links' : social_links,
        'contact' : contact,
        'reviews' : reviews,
    }
    return render(request, 'website/reviews.html', context)


def courses(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    courses_categories = CourseCategory.objects.all()
    courses = Course.objects.all()
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'courses_categories' : courses_categories,
        'courses' : courses,
    }
    return render(request, 'website/courses.html', context)


def courseDetail(request, pk):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    course = Course.objects.get(id=pk)
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'course' : course,
    }
    return render(request, 'website/course-detail.html', context)


def faqs(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    a = FAQ.objects.all()
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'a' : a,
    }
    return render(request, 'website/faqs.html', context)


def contact(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
    }
    return render(request, 'website/contact.html', context)


def territories(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    trritories = CoverageArea.objects.all()
    cities = CoverageAreaCity.objects.all()
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'territories' : trritories,
        'cities' : cities,
    }
    return render(request, 'website/territories.html', context)



def instructorRegistration(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    why_join_us = WhyJoinUs.objects.all()
    
    form = InstructorForm()
    user_form = UserCreationForm()
    
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES)
        user_form = UserCreationForm(request.POST)
        
        if form.is_valid() and user_form.is_valid():
            instructor = form.save(commit=False)
            
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()
            
            instructor.auth_login = user
            instructor.save()
            
            
            # Sending mail from here
            mail_context = {
                'instructor' : instructor,
            }
            a = render_to_string('website/email-template-for-instructor-request-for-admin.html', mail_context)
            template1 = strip_tags(a)
            
            email = EmailMultiAlternatives(
                f'New instructor request from {instructor.first_name} via {general_info.title} ', 
                template1, 
                settings.EMAIL_HOST_USER, 
                [settings.ADMIN_EMAIL],
                )
            email.attach_alternative(a, 'text/html')
            email.fail_silently = True
            try:
                email.send()
            except:
                pass
            
            
            messages.success(request, 'Your request is submitted successfuly')
            return redirect('website:instructor-registration')
        
        
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'why_join_us' : why_join_us,
        'form' : form,
        'user_form' : user_form,
    }
    return render(request, 'website/instructor-registration.html', context)





def booking(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    courses = Course.objects.all()
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    form = StudentRegistrationForm()
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        start_date = request.POST.get('start_date')
        fast_track_test = request.POST.get('fast_track_test')
        learning_difficulty = request.POST.get('learning_difficulty')
        courses_input = request.POST.getlist('courses')
        
        if form.is_valid():
            reg = form.save(commit=False)
            reg.start_date = start_date
            
            if fast_track_test:
                reg.fast_track_test = fast_track_test
            else:
                reg.fast_track_test = 0
                
            if learning_difficulty:
                reg.learning_difficulty = learning_difficulty
            else:
                reg.learning_difficulty = 0
                
            reg.registration_id = f"{form.cleaned_data['first_name'][0]}{form.cleaned_data['last_name'][0]}-{timestamp}-{form.cleaned_data['zip_code']}"
            reg.save()
            
            total_initial_deposit = 0
            for i in courses_input:
                course=get_object_or_404(Course, id=i)
                
                StudentRegistrationCourse.objects.create(
                    registration=reg,
                    course=course
                )
                total_initial_deposit += course.advance_deposit
                
            reg.total_initial_deposit = total_initial_deposit
            reg.save()
                
            messages.success(request, 'Please deposit the advance amount to continue')
            return redirect('website:make-payment', reg.registration_id)
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'form' : form,
        'courses' : courses,
    }
    return render(request, 'website/registration/1.html', context)




def registrationPayment(request, reg_id):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    stripe_keys = StripeAccountKey.objects.first()
    
    instance = get_object_or_404(StudentRegistration, registration_id=reg_id)
    
    if instance.status == 2:
        return redirect(reverse('website:already-paid'))
        
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'instance' : instance,
        'stripe_public_key' : stripe_keys.stripe_public_key,
    }
    return render(request, 'website/registration/2.html', context)




def CreateCheckoutSession(request):
    stripe_keys = StripeAccountKey.objects.first()
    
    stripe.api_key = stripe_keys.stripe_secret_key
    
    instance = get_object_or_404(StudentRegistration, registration_id=request.POST.get('reg_id'))
    cp = GeneralInfo.objects.first()
    
    customer = stripe.Customer.create(
            email=request.POST.get('email'),
            name=request.POST.get('nickname'),
            source=request.POST.get('stripeToken')
            )
    
    try:
        stripe.Charge.create(
            customer=customer,
            amount=int(instance.total_initial_deposit)*100,
            currency='gbp',
            description=f"Payment by {instance.first_name} {instance.last_name} of registration ID {instance.registration_id}"
            )
    
    except:
        return redirect(reverse('website:cancel'))
        
    
    # changing registration status to paid
    instance.status = 2
    instance.save()
    
    

    # Sending html email from here
    context = {
        'cp' : cp,
        'instance' : instance,
        'nick' : request.POST.get('nickname'),
    }
    
    html_content = render_to_string("website/payment-confirmation-mail.html", context)
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(
        f'Payment Confirmation From {cp.title}',
        text_content,
        settings.EMAIL_HOST_USER,
        [instance.email, settings.ADMIN_EMAIL],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()
    
    return redirect(reverse('website:success', args=[instance.registration_id]))
    
    
    
    
    
    
def successMsg(request, args):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    instance = get_object_or_404(StudentRegistration, registration_id=args)
    
    if instance.status == 1:
        return redirect(reverse('website:make-payment', args=[instance.registration_id]))
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'instance' : instance
    }
    return render(request, 'website/registration/success.html', context)


def errorMsg(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    instance = get_object_or_404(StudentRegistration, registration_id=args)
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
        'instance' : instance,
    }
    return render(request, 'website/registration/cancel.html', context)


def alreadyPaid(request):
    general_info = GeneralInfo.objects.first()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()
    
    context = {
        'i' : general_info,
        'social_links' : social_links,
        'contact' : contact,
    }
    return render(request, 'website/registration/paid.html', context)
