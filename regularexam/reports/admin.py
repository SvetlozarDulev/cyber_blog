from django.contrib import admin
from .models import Report, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    #1 empty rows
    extra = 1

class ReportAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Report, ReportAdmin)
admin.site.register(Comment)

