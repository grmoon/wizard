from django.contrib import admin

from wizard.admin.fields import (
    CheckboxFieldAdmin,
    RadioButtonFieldAdmin,
    SelectFieldAdmin,
)
from wizard.models import (
    Answer,
    Question,
    CheckboxField,
    RadioButtonField,
    Option,
    Section,
    SelectField,
    Step,
    TextField,
    Trigger,
    Wizard,
)
from wizard.admin.section import SectionAdmin
from wizard.admin.step import StepAdmin
from wizard.admin.wizard import WizardAdmin
from wizard.admin.question import QuestionAdmin

admin.site.register(Answer)
admin.site.register(CheckboxField, CheckboxFieldAdmin)
admin.site.register(Option)
admin.site.register(Question, QuestionAdmin)
admin.site.register(RadioButtonField, RadioButtonFieldAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SelectField, SelectFieldAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(TextField)
admin.site.register(Trigger)
admin.site.register(Wizard, WizardAdmin)