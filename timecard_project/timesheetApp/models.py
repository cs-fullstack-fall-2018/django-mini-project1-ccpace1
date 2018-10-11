from django.db import models
from django.utils import timezone


class Timesheet(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    hours = models.IntegerField()
    dateOfWork = models.DateTimeField(default=timezone.now())
    dateofEntry = models.DateTimeField(default=timezone.now())