from django.contrib import admin

from wizard.admin.fields import (
    CheckboxFieldAdmin,
    RadioButtonFieldAdmin,
    SelectFieldAdmin,
)
from wizard.models import (
    CheckboxField,
    FileAnswer,
    FileField,
    FileQuestion,
    JSONAnswer,
    JSONQuestion,
    Option,
    RadioButtonField,
    Section,
    SelectField,
    Step,
    TextField,
    Trigger,
    Upload,
    Wizard,
)
from wizard.admin.section import SectionAdmin
from wizard.admin.step import StepAdmin
from wizard.admin.wizard import WizardAdmin
from wizard.admin.question import QuestionAdmin
from wizard.admin.answers.file_answer import FileAnswerAdmin

admin.site.register(CheckboxField, CheckboxFieldAdmin)
admin.site.register(FileAnswer, FileAnswerAdmin)
admin.site.register(FileField)
admin.site.register(FileQuestion)
admin.site.register(JSONAnswer)
admin.site.register(JSONQuestion)
admin.site.register(Option)
admin.site.register(RadioButtonField, RadioButtonFieldAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SelectField, SelectFieldAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(TextField)
admin.site.register(Trigger)
admin.site.register(Upload)
admin.site.register(Wizard, WizardAdmin)