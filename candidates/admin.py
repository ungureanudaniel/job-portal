from django.contrib import admin
from .models import Profile, Skill, SavedJobs, AvailableCountry, AppliedJobs
class ProfileAdmin(admin.ModelAdmin):
     list_display = ('full_name', 'country', 'location', 'resume', 'grad_year', 'looking_for', 'slug')

class SkillAdmin(admin.ModelAdmin):
     list_display =  ('skill',)

class SavedJobsAdmin(admin.ModelAdmin):
     list_display =  ['job']

class AppliedJobsAdmin(admin.ModelAdmin):
     list_display =  ['job']


class AvailableCountryAdmin(admin.ModelAdmin):
     list_display = ['name']

admin.site.register(AvailableCountry, AvailableCountryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SavedJobs, SavedJobsAdmin)
admin.site.register(AppliedJobs, AppliedJobsAdmin)
