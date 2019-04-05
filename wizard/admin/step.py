from django.contrib import admin

from wizard.models import Section


class SectionInline(admin.StackedInline):
    extra = 1
    model = Section
    show_change_link = True


class StepAdmin(admin.ModelAdmin):
    inlines = (
        SectionInline,
    )