from django.contrib import admin

from wizard.admin.options.checkbox import CheckboxOptionInline


class CheckboxFieldAdmin(admin.ModelAdmin):
    inlines = (
        CheckboxOptionInline,
    )