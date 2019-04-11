from django.contrib import admin

from wizard.admin.upload import UploadInline


class FileAnswerAdmin(admin.ModelAdmin):
    inlines = (
        UploadInline,
    )
