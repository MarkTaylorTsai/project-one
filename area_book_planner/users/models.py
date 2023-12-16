from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.EmailField(unique= True, blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "email"  
    REQUIRED_FIELDS = [] 

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name="customuser_groups",  # Use a unique related name
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name="customuser_permissions",  # Use a unique related name
        help_text='Specific permissions for this user.',
    )    

