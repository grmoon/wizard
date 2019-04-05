from django.contrib import admin

from wizard.models import Step


class StepInline(admin.StackedInline):
    extra = 1
    model = Step
    show_change_link = True


class WizardAdmin(admin.ModelAdmin):
    inlines = (
        StepInline,
    )