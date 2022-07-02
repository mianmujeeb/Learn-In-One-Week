from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from .functions import *
from .decorators import unauthenticated_user
from django.db.models import Q
from website.models import *
from .forms import *
from .filters import *
from website.forms import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.

@unauthenticated_user
def login(request):
    general_info = GeneralInfo.objects.all().first()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            
            messages.success(request, 'Welcome on the board')
            if 'next' in request.POST:
                return redirect("portal:request.POST['next']")
            else:
                return redirect('portal:dashboard')
        else:
            messages.warning(request, 'Invalid credentials')
    
    context = {
        'general_info' : general_info,
    }
    return render(request, 'portal/login.html', context)


def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('portal:login')


@login_required(login_url='portal:login')
def dashboard(request):
    general_info = GeneralInfo.objects.all().first()
    user_type = request.session.get('user_type')
    
    if user_type == 1 or user_type == 2:
        transactions = Transaction.objects.all().order_by('-date')[:5]
        users = User.objects.all().order_by('date_joined')[:5]
        
        
        context = {
            'general_info' : general_info,
            'transactions' : transactions,
            'users' : users,
        }
        
    else:
        context = {
            'general_info' : general_info,
        }
        
        
    return render(request, 'portal/dashboard.html', context)




@login_required(login_url='portal:login')
@permission_required('portal.change_stripe', raise_exception=True)
def stripAccountSetting(request):
    general_info = GeneralInfo.objects.all().first()
    instance = StripeAccountKey.objects.first()
    form = StripeAccountKeyForm(instance=instance)
    
    if request.method == 'POST':
        form = StripeAccountKeyForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Stripe account keys updated successfully')
            return redirect('portal:stripe-account-setting')
    
    context = {
        'general_info' : general_info,
        'instance' : instance,
        'form' : form,
    }
    return render(request, 'portal/settings/stripe-setting.html', context)



@login_required(login_url='portal:login')
@permission_required('website.view_course', raise_exception=True)
def courses(request):
    general_info = GeneralInfo.objects.all().first()
    courses = Course.objects.all().order_by('-id')
    
    context = {
        'general_info' : general_info,
        'courses' : courses,
    }
    return render(request, 'portal/courses/courses.html', context)



@login_required(login_url='portal:login')
@permission_required('website.add_course', raise_exception=True)
def addCourse(request):
    general_info = GeneralInfo.objects.all().first()
    form = CourseForm()
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully')
            return redirect('portal:courses')
    
    context = {
        'general_info' : general_info,
        'form' : form,
    }
    return render(request, 'portal/courses/add-course.html', context)




@login_required(login_url='portal:login')
@permission_required('website.change_course', raise_exception=True)
def updateCourse(request, pk):
    general_info = GeneralInfo.objects.all().first()
    instance = get_object_or_404(Course, id=pk)
    form = CourseForm(instance=instance)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully')
            return redirect('portal:courses')
    
    context = {
        'general_info' : general_info,
        'form' : form,
        'instance' : instance,
    }
    return render(request, 'portal/courses/update-course.html', context)




@login_required(login_url='portal:login')
@permission_required('website.delete_course', raise_exception=True)
def deleteCourse(request, pk):
    course = get_object_or_404(Course, id=pk)
    course.delete()
    messages.info(request, 'Course deleted successfully') 
    return redirect('portal:courses')



@login_required(login_url='portal:login')
@permission_required('website.view_instructor', raise_exception=True)
def instructorRequests(request):
    general_info = GeneralInfo.objects.all().first()
    instructors = Instructor.objects.filter(status=1).order_by('-id')
    
    context = {
        'general_info' : general_info,
        'instructors' : instructors,
    }
    return render(request, 'portal/instructor-requests/instructors-requests.html', context)


@login_required(login_url='portal:login')
@permission_required('website.view_instructor', raise_exception=True)
def updateInstructorRequests(request, pk):
    general_info = GeneralInfo.objects.all().first()
    instance = get_object_or_404(Instructor, id=pk, status=1)
    
    if request.method == 'POST':
        if 'approve' in request.POST:
            instance.status = 2
            instance.save()
            
            auth = instance.auth_login
            auth.is_active = True
            auth.save()
            
            messages.success(request, 'Instructor approved successfully')
            return redirect('portal:update-instructor', instance.id)
    
    context = {
        'general_info' : general_info,
        'instance' : instance,
    }
    return render(request, 'portal/instructor-requests/update-instructors-request.html', context)




@login_required(login_url='portal:login')
@permission_required('website.view_instructor', raise_exception=True)
def instructors(request):
    general_info = GeneralInfo.objects.all().first()
    instructors = Instructor.objects.filter(status=2).order_by('-id')
    
    context = {
        'general_info' : general_info,
        'instructors' : instructors,
    }
    return render(request, 'portal/instructors/instructors.html', context)




@login_required(login_url='portal:login')
@permission_required('website.view_instructor', raise_exception=True)
def updateInstructor(request, pk):
    general_info = GeneralInfo.objects.all().first()
    instance = get_object_or_404(Instructor, id=pk, status=2)
    
    form = InstructorForm(instance=instance)
    
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES, instance=instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor updated successfully')
            return redirect('portal:instructors')
    
    context = {
        'general_info' : general_info,
        'instance' : instance,
    }
    return render(request, 'portal/instructors/update-instructor.html', context)




@login_required(login_url='portal:login')
@permission_required('portal.view_studentregistration', raise_exception=True)
def registrations(request):
    general_info = GeneralInfo.objects.all().first()
    
    registrations = StudentRegistration.objects.all().order_by('-id')
    registrations = Paginator(registrations, 50)
    page_number = request.GET.get('page', 1)
    page = registrations.page(page_number)

    
    context = {
        'general_info' : general_info,
        'registrations' : page,
    }
    return render(request, 'portal/registrations/registrations.html', context)




@login_required(login_url='portal:login')
@permission_required('portal.view_studentregistration', raise_exception=True)
def viewRegistration(request, reg_id):
    general_info = GeneralInfo.objects.all().first()
    
    registration = get_object_or_404(StudentRegistration, registration_id=reg_id)

    
    context = {
        'general_info' : general_info,
        'instance' : registration,
    }
    return render(request, 'portal/registrations/view-registration.html', context)
