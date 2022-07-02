from django.contrib import admin
from website.models import *

# Register your models here.


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    
    list_display = ('phone_number', 'email')
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
    
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    
    list_display = ('name',)
    
    
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

    list_display = ('title',)
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ('title',)
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
    
    
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('name', 'category')
    list_filter = ('category',)
    
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = ('client_name',)
    
    
    
class CoverageAreaCityInline(admin.TabularInline):
    model = CoverageAreaCity
@admin.register(CoverageArea)
class CoverageAreaAdmin(admin.ModelAdmin):

    list_display = ('name',)
    inlines = [
        CoverageAreaCityInline,
    ]
    
    
@admin.register(Benifit)
class BenifitAdmin(admin.ModelAdmin):
    list_display = ('title',) 

    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    
    
@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):

    list_display = ('title',)
    
    
@admin.register(WhyJoinUs)
class WhyJoinUsAdmin(admin.ModelAdmin):

    list_display = ('title',)
    



@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'email')