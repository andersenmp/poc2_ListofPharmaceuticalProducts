from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone

from DjangoPython.core.models import AuditTrail


class MedicalList(AuditTrail):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    composition = models.CharField(max_length=250, null=True, blank=True)
    reimbursible = models.CharField(max_length=100, null=True, blank=True)
    usage = models.CharField(max_length=250, null=True, blank=True)
    comments = models.CharField(max_length=250, null=True, blank=True)
    app_date = models.DateField(auto_now=True)
    link = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-active', 'app_date']
