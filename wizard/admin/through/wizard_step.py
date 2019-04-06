from django.contrib import admin

from wizard.models import WizardStep


class WizardStepInline(admin.StackedInline):
    extra = 1
    model = WizardStep
    show_change_link = True
