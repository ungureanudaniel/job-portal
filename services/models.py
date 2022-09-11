from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from time import strftime, gmtime
from django.utils.text import slugify

#-----------------------------------THE JOB CATEGORIES MODEL-------------------
class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='media/job_category', blank=True, null=True)
    image = models.ImageField(upload_to='media/job_category', blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



#-----------------------------------THE JOB POST ------ ------------------------
# class SubCategory(models.Model):
#     cat = models.ForeignKey(Category, related_name='_category', on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=30)
#     slug = models.SlugField(max_length=255, unique=True)
#
#     class Meta:
#         verbose_name = 'subcategory'
#         verbose_name_plural = 'subcategories'
#
#     def __str__(self):
#         return self.name
# #-----------------------------------THE JOB CATEGORIES MODEL-------------------
# class Metadata(models.Model):
#     sub_category = models.ForeignKey(SubCategory, related_name='metadata', on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=30)
#     compulsory = models.BooleanField(default=False)
#     slug = models.SlugField(max_length=255, unique=True)
#
#     class Meta:
#         verbose_name = 'Metadata'
#         verbose_name_plural = 'Metadata'
#
#     def __str__(self):
#         return self.name
#
# #-----------------------------------THE JOB POST ------ ------------------------
# class MetaOptions(models.Model):
#     metadata = models.ForeignKey(Metadata, related_name='metaoptions', on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=30)
#     slug = models.SlugField(max_length=255, unique=True)
#
#     class Meta:
#         verbose_name = 'MetaOptions'
#         verbose_name_plural = 'MetaOptions'
#
#     def __str__(self):
#         return self.name
#---------------------------POST TAGS -----------------------------------------
class Tag(models.Model):
    name_ro = models.CharField(max_length=255, unique=True)
    name_en = models.CharField(max_length=255, unique=True)
    name_de = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name_ro
#
# #--------------------------CANDIDATE POST MODEL---------------------------------
class ServicePost(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog')
    text = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, blank=True, null=True)
    # subcat = models.ForeignKey(SubCategory, related_name='subcategory', on_delete=models.SET_NULL, blank=True, null=True)
    price_min = models.CharField(max_length=10)
    price_max = models.CharField(max_length=10)
    # metadata = models.ForeignKey(Metadata, related_name='metadata', on_delete=models.SET_NULL, blank=True, null=True)
    # meta_options = models.ManyToManyField(MetaOptions, blank=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Published', choices=STATUS_CHOICES)
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ["-created_date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(ServicePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            # 'id': pk.self
        }
        return reverse('add_post', kwargs=kwargs)

    def __str__(self):
        return self.title
#--------------------------------TESTIMONIALS MODEL----------------------------
class Review(models.Model):
    name = models.CharField(max_length=20)
    text = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='media', blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Review, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name


#----------------------------------Profile model ----------------------------
class Profile(models.Model):
    CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    )
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    full_name = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    grad_year = models.IntegerField(blank=True)
    looking_for = models.CharField(max_length=30, choices=CHOICES, default='Full Time', null=True)
    slug = AutoSlugField(populate_from='user', unique=True)

    def get_absolute_url(self):
        return "/profile/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
#----------------------------------Skills model ----------------------------
class Skill(models.Model):
    skill = models.CharField(max_length=200)
#----------------------------------News category model ----------------------------
class NewsCategory(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'
    def __str__(self):
        return self.name
#----------------------------------News model ----------------------------
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news')
    text = RichTextField(blank=True, null=True)
    category = models.ForeignKey(NewsCategory, related_name='newscategory', on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
