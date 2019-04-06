from django.contrib import admin

from wizard.admin.through import TriggerInline
from wizard.models import SectionQuestion


class QuestionAdmin(admin.ModelAdmin):
    inlines = (
        TriggerInline,
    )
