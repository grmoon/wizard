from django.contrib import admin

from wizard.models import Trigger


class TriggerInline(admin.StackedInline):
    extra = 1
    model = Trigger
    show_change_link = True
    fk_name = 'from_question'
