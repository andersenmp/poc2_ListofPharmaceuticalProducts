from django.contrib import admin
from .models import *


class SentryAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name', 'last_name', 'email','feature', 'org_id', 'access_mode')


admin.site.register(SentryModel, SentryAdmin)

