from django.urls import path
from django.urls import reverse_lazy
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('', dashboard, name='dashboard'),
    
    path('stripe-account-setting', stripAccountSetting, name='stripe-account-setting'),
    
    # Courses routes
    path('courses', courses, name='courses'),
    path('course/add', addCourse, name='add-course'),
    path('course/update/<int:pk>', updateCourse, name='update-course'),
    path('course/delete/<int:pk>', deleteCourse, name='delete-course'),
    
    # Instructors routes
    path('instructor-requests', instructorRequests, name='instructor-requests'),
    path('instructor-request/update/<int:pk>', updateInstructorRequests, name='update-instructor-request'),
    
    # Instructors routes
    path('instructors', instructors, name='instructors'),
    path('instructor/update/<int:pk>', updateInstructor, name='update-instructor'),
    
    # Registrtions routes 
    path('registrations', registrations, name='registrations'),
    path('registration/view/<str:reg_id>', viewRegistration, name='view-registration'),
    
    
    # Reset password routes
    path('password/reset', 
            auth_views.PasswordResetView.as_view(
                template_name='portal/password/password-reset.html',
                email_template_name = 'portal/password/password-reset-email.html', 
                success_url=reverse_lazy('portal:password_reset_done')),
            name='reset_password'),
    
    path('password/reset/sent',
            auth_views.PasswordResetDoneView.as_view(
                template_name='portal/password/password-reset-sent.html'), 
            name='password_reset_done'),
    
    path('password/reset/confirm/<uidb64>/<token>', 
            auth_views.PasswordResetConfirmView.as_view(
                template_name='portal/password/password-reset-form.html',
                success_url=reverse_lazy('portal:password_reset_complete')),
            name='password_reset_confirm'),
    
    path('password/reset/complete', 
            auth_views.PasswordResetCompleteView.as_view(
                template_name='portal/password/password-reset-complete.html'), 
            name='password_reset_complete'),
]