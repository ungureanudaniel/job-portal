from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from recruiters.models import JobCategory, Job
from ckeditor.fields import RichTextField

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None

class AvailableCountry(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name = "Available Countries")

    class Meta:
        verbose_name = "Available Country"
        verbose_name_plural = "Available Countries"

    def __str__(self):
        return self.name
#---------------------------POST TAGS -----------------------------------------
class Tag(models.Model):
    name_ro = models.CharField(max_length=255, unique=True)
    name_en = models.CharField(max_length=255, unique=True)
    name_de = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name_ro

#--------------------------CANDIDATE POST MODEL---------------------------------

class Post(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog')
    text = RichTextField(blank=True, null=True)
    category = models.ForeignKey(JobCategory, related_name='jobcategory', on_delete=models.SET_NULL, blank=True, null=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Published', choices=STATUS_CHOICES)
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ["-created_date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            # 'id': pk.self
        }
        return reverse('add_post', kwargs=kwargs)

    def __str__(self):
        return self.title

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

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    # user = models.ForeignKey(CustomUser, related_name='skills', on_delete=models.CASCADE)
#
class SavedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='saved_job', on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = "Saved Jobs"
        verbose_name_plural = "Saved Jobs"

    def __str__(self):
        return self.job.title

class AppliedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='applied_job', on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Applied Jobs"
        verbose_name_plural = "Applied Jobs"

    def __str__(self):
        return self.job.title
