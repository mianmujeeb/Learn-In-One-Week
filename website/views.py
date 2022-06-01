from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    general_info = GeneralInfo.objects.first()
    courses_categories = CourseCategory.objects.all()
    social_links = SocialLink.objects.all()
    about_us = About.objects.first()
    contact = ContactInfo.objects.first()
    why_us = WhyUs.objects.all()
    stats = Stats.objects.first()
    testimonials = Testimonial.objects.all()
    
    
    context = {
        'i' : general_info,
        'j' : courses_categories,
        'social_links' : social_links,
        'testimonials' : testimonials,
        'about' : about_us,
        'why_us' : why_us,
        'stats' : stats,
        'contact' : contact,
    }
    return render(request, 'website/index.html', context)



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