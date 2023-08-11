from django.db import models

class ScanningLink(models.Model):
    url = models.URLField()