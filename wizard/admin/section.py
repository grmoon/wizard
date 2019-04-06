from django.contrib import admin

from wizard.models import SectionQuestion
from wizard.admin.section_question import SectionQuestionInline


class SectionAdmin(admin.ModelAdmin):
    inlines = (
        SectionQuestionInline,
    )