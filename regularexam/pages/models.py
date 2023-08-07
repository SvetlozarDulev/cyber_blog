from django.db import models
from django.urls import reverse


# Create your models here.

class EducationalMaterials(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False)
    description = models.CharField(blank=True,null=True,max_length=400)
    url = models.URLField(blank=False,null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('education-list')

class GiveBestAdvice(models.Model):
    text = models.TextField(max_length=300)

    def get_absolute_url(self):
        return reverse('best-advice')