from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone
from time import strftime
from time import gmtime


# #-----------------------------------THE JOB CATEGORIES MODEL-------------------
class JobCategory(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='media/job_category', blank=True, null=True)
    image = models.ImageField(upload_to='media/job_category', blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    @classmethod
    def get_default_pk(cls):
        cat, created = cls.objects.get_or_create(
            name='default category')
        return cat.pk

    def __str__(self):
        return self.name

#
#
# #-----------------------------------THE JOB POST ------ ------------------------
class Job(models.Model):
    CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    )
    # recruiter = models.ForeignKey(CustomUser, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos')
    country = CountryField(null=True, blank=True)
    locality = models.CharField(max_length=200)
    description = models.TextField()
    skills_req = models.CharField(max_length=200)
    category = models.ForeignKey(JobCategory, related_name='job_category', on_delete=models.CASCADE, default=JobCategory.get_default_pk)
    job_type = models.CharField(max_length=30, choices=CHOICES, default='Full Time', null=True)
    from_wage_hour = models.IntegerField(null=True)
    to_wage_hour = models.IntegerField(null=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
       ordering = ['-date_posted']

    def get_time_diff(self):
        if self.date_posted:
            now = datetime.datetime.utcnow().replace(tzinfo=timezone.utc)
            timediff = (now - self.date_posted).total_seconds()
            return strftime("%H", gmtime(timediff))

    def __str__(self):
        return self.title


class Applicant(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    # applicant = models.ForeignKey(CustomUser, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(Job, related_name='select_job', on_delete=models.CASCADE)
    # applicant = models.ForeignKey(CustomUser, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Selected"
        verbose_name_plural = "Selected"

    def __str__(self):
        return self.applicant
