from django.contrib import admin

from wizard.models import Upload


class UploadInline(admin.StackedInline):
    extra = 1
    model = Upload
    show_change_link = True
