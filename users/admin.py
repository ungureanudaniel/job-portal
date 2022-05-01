from django.contrib import admin
from .models import BlogPostCategory, BlogPost, Testimonial, Users

class BlogPostCategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'image', 'slug')
     prepopulated_fields = {'slug': ('name',)}

class BlogPostAdmin(admin.ModelAdmin):
     list_display =  ('title', 'image', 'text', 'category', 'views_count', 'comment_count', 'featured', 'slug', 'created_date', 'status')
     prepopulated_fields = {'slug': ('title',)}

class TestimonialAdmin(admin.ModelAdmin):
     list_display =  ['name', 'text', 'image']

class UsersAdmin(admin.ModelAdmin):
     list_display =  ['user', 'email', 'phone', 'confirmed','type', 'conf_number']


admin.site.register(BlogPostCategory, BlogPostCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Users, UsersAdmin)
