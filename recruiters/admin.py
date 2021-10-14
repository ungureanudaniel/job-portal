from django.contrib import admin
from .models import Job, Applicant, Selected


class JobAdmin(admin.ModelAdmin):
     list_display = ('recruiter', 'title', 'company', 'logo', 'location', 'description', 'skills_req', 'job_type', 'from_wage_hour', 'to_wage_hour', 'link', 'slug')

class ApplicantAdmin(admin.ModelAdmin):
     list_display =  ('job', 'applicant', 'date_posted')

class SelectedAdmin(admin.ModelAdmin):
     list_display =  ('job', 'applicant', 'date_posted')


admin.site.register(Job, JobAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Selected, SelectedAdmin)
