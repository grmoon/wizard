from django.contrib import admin

from wizard.models import Question


class QuestionInline(admin.StackedInline):
    extra = 1
    model = Question
    show_change_link = True


class SectionAdmin(admin.ModelAdmin):
    inlines = (
        QuestionInline,
    )