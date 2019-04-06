from django.contrib import admin

from wizard.models import RadioButtonFieldOption


class RadioButtonFieldOptionInline(admin.StackedInline):
    extra = 1
    model = RadioButtonFieldOption
    show_change_link = True
