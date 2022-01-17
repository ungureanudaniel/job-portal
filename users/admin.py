from django.contrib import admin
from .models import BlogPostCategory, BlogPost, Testimonial, Candidate, Company

class BlogPostCategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'image', 'slug')
     prepopulated_fields = {'slug': ('name',)}

class BlogPostAdmin(admin.ModelAdmin):
     list_display =  ('author', 'title', 'image', 'text', 'category', 'views_count', 'comment_count', 'featured', 'slug', 'created_date', 'status')
     prepopulated_fields = {'slug': ('title',)}

class TestimonialAdmin(admin.ModelAdmin):
     list_display =  ['name', 'text', 'image']

class CandidateAdmin(admin.ModelAdmin):
     list_display =  ['user', 'email', 'phone', 'confirmed', 'gender', 'birthdate', 'type', 'conf_number']

class CompanyAdmin(admin.ModelAdmin):
     list_display =  ['user', 'email', 'phone', 'confirmed', 'company_name', 'type', 'identification', 'conf_number']

admin.site.register(BlogPostCategory, BlogPostCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Company, CompanyAdmin)
