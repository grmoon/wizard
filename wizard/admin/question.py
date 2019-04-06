from django.contrib import admin

from wizard.models import SectionQuestion
from wizard.admin.section_question import SectionQuestionInline


class QuestionAdmin(admin.ModelAdmin):
    inlines = (
        SectionQuestionInline,
    )