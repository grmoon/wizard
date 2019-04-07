from django.contrib import admin

from wizard.models import CheckboxFieldOption


class CheckboxFieldOptionInline(admin.StackedInline):
    extra = 1
    model = CheckboxFieldOption
    show_change_link = True
