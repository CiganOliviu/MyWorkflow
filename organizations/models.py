from django.db import models


class GithubOrganization(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    gmail = models.CharField(max_length=50)
    description = models.TextField()
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    picture = models.ImageField(upload_to='organizations/', default='/organizations/default.jpg')

    def __str__(self):
        return self.name
