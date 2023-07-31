from django.utils import timezone

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MaxValueValidator
# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    additional_materials = models.URLField()
    common_vulnerability_scoring_system = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(limit_value=10)]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('report_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('report_list')
