from django.contrib import admin
from .models import *


class MedicalListAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition', 'reimbursible', 'usage','app_date')


admin.site.register(MedicalList, MedicalListAdmin)
