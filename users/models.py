from django.db import models

# Create your models here.
#----------------------------------ABOUT ME MODEL
class About(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=600)
    image1 = models.ImageField(upload_to='about_image', blank=True)
    image2 = models.ImageField(upload_to='about_image', blank=True)
    image3 = models.ImageField(upload_to='about_image', blank=True)

    def __str__(self):
        return self.title
