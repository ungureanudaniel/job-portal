from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

#--------------------------------TESTIMONIALS MODEL----------------------------
class Testimonial(models.Model):
    name = models.CharField(max_length=20)
    text = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='media', blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Testimonial, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
