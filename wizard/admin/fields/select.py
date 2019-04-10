from django.contrib import admin

from wizard.admin.options.select import SelectOptionInline


class SelectFieldAdmin(admin.ModelAdmin):
    inlines = (
        SelectOptionInline,
    )