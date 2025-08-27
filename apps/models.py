# apps/models.py

from django.db import models
from django.utils import timezone


class Provider(models.TextChoices):
    SALESFORCE = 'salesforce'
    GOOGLE_ANALYTICS = 'ga'
    GOOGLE_ADS = 'gads'
    META = 'meta'
    MICROSOFT = 'microsoft'
    X = 'x'


class Lead(models.Model):
    external_id = models.CharField(max_length=255, unique=True)
    provider = models.CharField(max_length=32, choices=Provider.choices)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    data = models.JSONField(default=dict)
    last_updated = models.DateTimeField(default=timezone.now)
    last_synced = models.DateTimeField(null=True, blank=True)

    def mark_synced(self):
        self.last_synced = timezone.now()
        self.save(update_fields=['last_synced'])


class Campaign(models.Model):
    external_id = models.CharField(max_length=255, unique=True)
    provider = models.CharField(max_length=32, choices=Provider.choices)
    name = models.CharField(max_length=255)
    data = models.JSONField(default=dict)
    last_updated = models.DateTimeField(default=timezone.now)
    last_synced = models.DateTimeField(null=True, blank=True)

    def mark_synced(self):
        self.last_synced = timezone.now()
        self.save(update_fields=['last_synced'])
