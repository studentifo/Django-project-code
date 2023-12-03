from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    LINK_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    ]

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_CHOICES)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)
