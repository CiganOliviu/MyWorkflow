from django.db import models
from .data_structures import IMPORTANCE_LEVEL


class CurrentActivitie(models.Model):
    activity = models.CharField(max_length=25, default="None", blank=False)
    importance_level = models.CharField(max_length=25, choices=IMPORTANCE_LEVEL, default="None", blank=False)
    short_description = models.TextField(default="None", blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.activity
