from django.contrib import admin

from wizard.admin.fields import (
    RadioButtonFieldAdmin
)
from wizard.models import (
    RadioButtonField,
    RadioButtonOption,
    Question,
)

admin.site.register(RadioButtonField, RadioButtonFieldAdmin)
admin.site.register(RadioButtonOption)
admin.site.register(Question)