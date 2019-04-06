from django.contrib import admin

from wizard.admin.through import StepSectionInline
from wizard.models import Section



class StepAdmin(admin.ModelAdmin):
    inlines = (
        StepSectionInline,
    )