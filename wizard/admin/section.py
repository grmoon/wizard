from django.contrib import admin

from wizard.admin.through import SectionQuestionInline
from wizard.models import SectionQuestion


class SectionAdmin(admin.ModelAdmin):
    inlines = (
        SectionQuestionInline,
    )