from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    years_experience = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
    )

