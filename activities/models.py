from django.db import models
from .data_structures import IMPORTANCE_LEVEL
from projects.models import PersonalProject


class CurrentActivitie(models.Model):
    project = models.ForeignKey(PersonalProject, on_delete=models.CASCADE, default=0)
    activity = models.CharField(max_length=25, default="None", blank=False)
    importance_level = models.CharField(max_length=25, choices=IMPORTANCE_LEVEL, default="None", blank=False)
    short_description = models.TextField(default="None", blank=False)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.activity
