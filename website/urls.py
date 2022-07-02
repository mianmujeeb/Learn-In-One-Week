from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    
    path("courses", courses, name="courses"),
    path("course/detail/<int:pk>", courseDetail, name="course-detail"),
    
    path("faqs", faqs, name="faqs"),
    
    path("reviews", reviews, name="reviews"),
    
    path("contact", contact, name="contact"),
    
    path("territories", territories, name="territories"),
    
    path("be-an-instructor", instructorRegistration, name="instructor-registration"),
    
    
    path("booking", booking, name="booking"),
    path('make-payment/<str:reg_id>', registrationPayment, name='make-payment'),
    path('charge', CreateCheckoutSession, name='charge'),
    path('success/<str:args>', successMsg, name='success'),
    path('error', errorMsg, name='cancel'),
    path('paid', alreadyPaid, name='already-paid'),
    
]
