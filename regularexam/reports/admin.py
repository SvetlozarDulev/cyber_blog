from django.contrib import admin
from .models import Report
# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "common_vulnerability_scoring_system",
    ]

admin.site.register(Report,ReportAdmin)