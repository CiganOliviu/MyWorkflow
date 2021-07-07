from django.contrib import admin
from .models import GithubOrganization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'gmail', 'website_url')


admin.site.register(GithubOrganization, OrganizationAdmin)
