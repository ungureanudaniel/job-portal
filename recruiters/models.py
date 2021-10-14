from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone
from time import strftime
from time import gmtime

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)


class Job(models.Model):
    recruiter = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos')
    location = models.CharField(max_length=255)
    description = models.TextField()
    skills_req = models.CharField(max_length=200)
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
            return strftime("%H:%M:%S", gmtime(timediff))

    def __str__(self):
        return self.title


class Applicant(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Selected"
        verbose_name_plural = "Selected"

    def __str__(self):
        return self.applicant
