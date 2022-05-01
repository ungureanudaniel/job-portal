from django.contrib import admin
from .models import Job, Applicant, Selected, JobCategory


class JobAdmin(admin.ModelAdmin):
     list_display = ('title', 'company', 'logo', 'description', 'category', 'skills_req', 'job_type', 'from_wage_hour', 'to_wage_hour', 'link', 'slug',)

class ApplicantAdmin(admin.ModelAdmin):
     list_display =  ('job', 'date_posted')

class SelectedAdmin(admin.ModelAdmin):
     list_display =  ('job', 'date_posted')

class JobCategoryAdmin(admin.ModelAdmin):
     list_display =  ('name', 'image', 'slug')
     prepopulated_fields = {'slug': ('name',)}



admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Selected, SelectedAdmin)
