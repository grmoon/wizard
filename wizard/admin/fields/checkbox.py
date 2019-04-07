from django.contrib import admin

from wizard.admin.fields.option import OptionInline
from wizard.admin.through import CheckboxFieldOptionInline


class CheckboxFieldAdmin(admin.ModelAdmin):
    inlines = (
        CheckboxFieldOptionInline,
    )