from django.db import models


class SentryModel(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    feature = models.CharField(max_length=250, null=True, blank=True)
    org_id = models.BigIntegerField(null=True,blank=True)
    access_mode = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.login
