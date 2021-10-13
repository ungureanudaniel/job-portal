from django.contrib import admin
from .models import Job, Applicants, Selected


class JobAdmin(admin.ModelAdmin):
     list_display = ('recruiter', 'title', 'company', 'location', 'description', 'skills_req', 'job_type', 'link', 'slug')

class ApplicantsAdmin(admin.ModelAdmin):
     list_display =  ('job', 'applicant', 'date_posted')

class SelectedAdmin(admin.ModelAdmin):
     list_display =  ('job', 'applicant', 'date_posted')


admin.site.register(Job, JobAdmin)
admin.site.register(Applicants, ApplicantsAdmin)
admin.site.register(Selected, SelectedAdmin)
