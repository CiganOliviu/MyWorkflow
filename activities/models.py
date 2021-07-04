from django.db import models


class CurrentActivitie(models.Model):
    activity = models.CharField(max_length=25, default="None", blank=False)
    importance_level = models.CharField(max_length=25, default="None", blank=False)
    short_description = models.TextField(default="None", blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.activity
