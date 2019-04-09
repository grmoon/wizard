from django.contrib import admin

from wizard.admin.fields.option import OptionInline
from wizard.admin.options.radio_button import RadioButtonOptionInline


class RadioButtonFieldAdmin(admin.ModelAdmin):
    inlines = (
        RadioButtonOptionInline,
    )