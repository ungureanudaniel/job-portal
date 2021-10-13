from django.contrib import admin
from .models import Profile, Skill, SavedJobs, AppliedJobs

class ProfileAdmin(admin.ModelAdmin):
     list_display = ('user', 'full_name', 'country', 'location', 'resume', 'grad_year', 'looking_for', 'slug')

class SkillAdmin(admin.ModelAdmin):
     list_display =  ('skill', 'user')

class SavedJobsAdmin(admin.ModelAdmin):
     list_display =  ['job', 'user']

class AppliedJobsAdmin(admin.ModelAdmin):
     list_display =  ['job', 'user']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SavedJobs, SavedJobsAdmin)
admin.site.register(AppliedJobs, AppliedJobsAdmin)
