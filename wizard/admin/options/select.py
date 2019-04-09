from django.contrib import admin

from wizard.models import SelectOption


class SelectOptionInline(admin.StackedInline):
    extra = 1
    model = SelectOption
    show_change_link = True
