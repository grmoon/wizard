from django.contrib import admin

from wizard.admin.fields.option import OptionInline
from wizard.admin.through import RadioButtonFieldOptionInline


class RadioButtonFieldAdmin(admin.ModelAdmin):
    inlines = (
        RadioButtonFieldOptionInline,
    )