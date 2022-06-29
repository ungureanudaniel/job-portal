from django.contrib import admin
from .models import Profile, Skill, Category, SubCategory

class ProfileAdmin(admin.ModelAdmin):
     list_display = ('full_name', 'country', 'location', 'resume', 'grad_year', 'looking_for', 'slug')

class SkillAdmin(admin.ModelAdmin):
     list_display =  ('skill',)

class SubCategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'image', 'slug')
     prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
     list_display =  ('name', 'image', 'slug')
     prepopulated_fields = {'slug': ('name',)}
#
#
#
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
