from django.contrib import admin

from wizard.admin.through import WizardStepInline
from wizard.models import Step


class WizardAdmin(admin.ModelAdmin):
    inlines = (
        WizardStepInline,
    )