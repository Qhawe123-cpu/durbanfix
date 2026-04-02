from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('issue_type', 'location', 'status', 'created_at')
    list_filter = ('status', 'issue_type')
    search_fields = ('location', 'description')