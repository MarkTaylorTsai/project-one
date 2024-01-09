from django.db import models

class MyUser(models.Model):
    name   = models.CharField(default="Your name", max_length=20)
    gender = models.CharField(default='Your gender')
    age    = models.IntegerField(blank=False, null=False)
    email  = models.EmailField(unique=True)