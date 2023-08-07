from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=40)
    email = models.EmailField(blank=True, unique=True)
    years_experience = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
    )


