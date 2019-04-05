from django.contrib import admin

from wizard.admin.fields import (
    RadioButtonFieldAdmin
)
from wizard.models import (
    Answer,
    RadioButtonField,
    RadioButtonOption,
    Question,
)

admin.site.register(Answer)
admin.site.register(RadioButtonField, RadioButtonFieldAdmin)
admin.site.register(RadioButtonOption)
admin.site.register(Question)