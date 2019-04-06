from django.contrib import admin

from wizard.models import Option


class OptionInline(admin.StackedInline):
    extra = 1
    model = Option
    show_change_link = True
