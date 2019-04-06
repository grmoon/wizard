from django.contrib import admin

from wizard.models import StepSection


class StepSectionInline(admin.StackedInline):
    extra = 1
    model = StepSection
    show_change_link = True
