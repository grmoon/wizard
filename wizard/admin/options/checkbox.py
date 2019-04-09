from django.contrib import admin

from wizard.models import CheckboxOption


class CheckboxOptionInline(admin.StackedInline):
    extra = 1
    model = CheckboxOption
    show_change_link = True
