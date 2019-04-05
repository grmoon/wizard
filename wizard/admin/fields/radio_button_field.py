from django.contrib import admin

from wizard.models import RadioButtonOption


class RadioButtonOptionInline(admin.StackedInline):
    extra = 1
    model = RadioButtonOption
    show_change_link = True


class RadioButtonFieldAdmin(admin.ModelAdmin):
    inlines = (
        RadioButtonOptionInline,
    )