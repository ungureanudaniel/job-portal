from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
# Create your models here.
#-----------------------------------THE POST CATEGORIES MODEL-------------------
class BlogPostCategory(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='media', blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'BlogCategory'
        verbose_name_plural = 'BlogCategories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(BlogPostCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name

#----------------------------------THE POST MODEL WITH ALL DETAILS--------------
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='blog_image', blank=True)
    text = RichTextField(blank=True, null=True)
    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE, related_name='postcategory')
    comment_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    featured = models.BooleanField()
    #seo_title = models.CharField(max_length=60, blank=True, null=True)
    #seo_text = models.CharField(max_length=165, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    #updated_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
        #return reverse('home')

    def get_edit_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})
        #return reverse('home')

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'pk': self.pk})
        #return reverse('home')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(BlogPost, self).save(*args, **kwargs)
