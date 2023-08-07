from django.contrib import admin
from .models import Report, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ReportAdmin(admin.ModelAdmin):
    list_display = ['title','author']
    inlines = [
        CommentInline,
    ]


admin.site.register(Report, ReportAdmin)
admin.site.register(Comment)

