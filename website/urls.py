from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    
    path("courses", courses, name="courses"),
    path("course/detail/<int:pk>", courseDetail, name="course-detail"),
    
    path("faqs", faqs, name="faqs"),
    
    path("contact", contact, name="contact"),
    
    path("territories", territories, name="territories"),
]
