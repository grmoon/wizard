from django.contrib import admin

from wizard.models import SectionQuestion


class SectionQuestionInline(admin.StackedInline):
    extra = 1
    model = SectionQuestion
    show_change_link = True


class SectionAdmin(admin.ModelAdmin):
    inlines = (
        SectionQuestionInline,
    )