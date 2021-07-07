from django.contrib import admin
from .models import GithubOrganization, BusinessModel


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'gmail', 'website_url')


class BusinessModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'posture')


admin.site.register(GithubOrganization, OrganizationAdmin)
admin.site.register(BusinessModel, BusinessModelAdmin)
