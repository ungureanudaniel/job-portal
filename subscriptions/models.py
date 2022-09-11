from django.db import models

# Create your models here.
#-----------------------------------Newsletter MODEL----------------------------
class Subscriber(models.Model):
    email = models.EmailField(max_length=200)
    # name = models.EmailField(max_length=200)
    conf_num =  models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
