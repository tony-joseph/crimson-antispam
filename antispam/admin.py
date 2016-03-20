from django.contrib import admin

from .models import SpamIP


@admin.register(SpamIP)
class SpamIPAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'created_on']
    search_fields = ['ip_address']
