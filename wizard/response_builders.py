from collections import namedtuple

from wizard.models import (
    Answer,
    CheckboxField,
    CheckboxOption,
    Field,
    MultipleChoiceField,
    Option,
    Question,
    RadioButtonField,
    RadioButtonOption,
    Section,
    SectionQuestion,
    SelectField,
    SelectOption,
    Step,
    StepSection,
    TextField,
    Trigger,
    WizardStep,
)

from wizard.serializers import (
    AnswerSerializer,
    OptionSerializer,
    FieldSerializer,
    QuestionSerializer,
    SectionQuestionSerializer,
    SectionSerializer,
    StepSectionSerializer,
    StepSerializer,
    TriggerSerializer,
    MultipleChoiceOptionSerializer,
    WizardStepSerializer,
)

MultipleChoiceFieldMapping = namedtuple('FieldMapping', ('field_class', 'option_class'))

class WizardStepResponseBuilder(object):
    FIELDS = (
        CheckboxField,
        RadioButtonField,
        SelectField,
        TextField,
    )

    MULTIPLE_CHOICE_FIELD_MAPPINGS = (
        MultipleChoiceFieldMapping(field_class=CheckboxField, option_class=CheckboxOption),
        MultipleChoiceFieldMapping(field_class=RadioButtonField, option_class=RadioButtonOption),
        MultipleChoiceFieldMapping(field_class=SelectField, option_class=SelectOption),
    )

    @classmethod
    def build(cls, user, wizard_id, step_num):
        wizard_step = cls._get_wizard_step_for_wizard(wizard_id, step_num)
        step = wizard_step.step
        step_sections = cls._get_step_sections_for_step(step)
        sections = step.sections.all()
        section_questions = cls._get_section_questions_for_sections(sections)
        questions = cls._get_questions_for_section_questions(section_questions)
        triggers = cls._get_triggers_from_questions(questions)
        answers = cls._get_answers_from_questions(user, questions)

        field_pks = questions.values_list('field_id', flat=True)
        fields = cls._get_fields_from_pks(field_pks)
        (options, multiple_choice_options) = cls._get_options_from_field_pks(field_pks)

        return {
            'wizard_step': WizardStepSerializer(wizard_step).data,
            'step': StepSerializer(step).data,
            'step_sections': StepSectionSerializer(step_sections, many=True).data,
            'sections': SectionSerializer(sections, many=True).data,
            'section_questions': SectionQuestionSerializer(section_questions, many=True).data,
            'questions': QuestionSerializer(questions, many=True).data,
            'triggers': TriggerSerializer(triggers, many=True).data,
            'fields': FieldSerializer(fields, many=True).data,
            'answers': AnswerSerializer(answers, many=True).data,
            'multiple_choice_options': MultipleChoiceOptionSerializer(multiple_choice_options, many=True).data,
            'options': OptionSerializer(options, many=True).data,
        }

    @staticmethod
    def _get_wizard_step_for_wizard(wizard_id, step_num):
        return WizardStep.objects\
            .select_related('step')\
            .prefetch_related('step__sections')\
            .prefetch_related('step__sections__questions')\
            .filter(wizard_id=wizard_id)[step_num - 1]

    @staticmethod
    def _get_step_sections_for_step(step):
        return StepSection.objects\
            .filter(step=step)\
            .all()

    @staticmethod
    def _get_section_questions_for_sections(sections):
        return SectionQuestion.objects\
            .filter(section__in=sections)\
            .all()

    @staticmethod
    def _get_questions_from_pks(question_pks):
        return Question.objects\
            .prefetch_related('triggers')\
            .filter(pk__in=question_pks)\
            .all()

    @classmethod
    def _get_questions_for_section_questions(cls, section_questions):
        question_pks = section_questions.values_list('question_id', flat=True)

        questions_from_section_questions = cls._get_questions_from_pks(question_pks)
        questions_from_triggers = cls._get_questions_for_question_triggers(questions_from_section_questions)

        return questions_from_section_questions | questions_from_triggers

    @classmethod
    def _get_questions_for_question_triggers(cls, questions):
        to_question_pks = questions.values_list('triggers', flat=True)
        to_questions = cls._get_questions_from_pks(to_question_pks)

        if to_questions.exists():
            questions = to_questions | cls._get_questions_for_question_triggers(to_questions)
        else:
            questions = to_questions

        return questions

    @staticmethod
    def _get_triggers_from_questions(questions):
        return Trigger.objects.filter(from_question__in=questions).all()

    @classmethod
    def _get_fields_from_pks(cls, field_pks):
        fields = list()

        for field_class in cls.FIELDS:
            fields += list(cls._get_fields(field_class, field_pks))

        return fields

    def _get_fields(field_class, field_pks):
        return field_class.objects.filter(pk__in=field_pks)

    @staticmethod
    def _get_answers_from_questions(user, questions):
        answer_pks = questions.values_list('answers__pk', flat=True)

        return Answer.objects.filter(pk__in=answer_pks, user=user).all()

    @classmethod
    def _get_options_from_field_pks(cls, field_pks):
        multiple_choice_options = list()
        option_pks = set()

        for mapping in cls.MULTIPLE_CHOICE_FIELD_MAPPINGS:
            _multiple_choice_options, _option_pks = cls._get_multiple_choice_options(
                field_pks,
                mapping.field_class,
                mapping.option_class
            )

            multiple_choice_options += list(_multiple_choice_options)
            option_pks.update(_option_pks)

        options = Option.objects.filter(pk__in=option_pks)

        return (options, multiple_choice_options)

    @staticmethod
    def _get_multiple_choice_options(field_pks, field_class, option_class):
        option_pks = field_class.objects\
            .filter(pk__in=field_pks)\
            .values_list('options', flat=True)\
            .all()

        multiple_choice_options = option_class.objects.filter(option_id__in=option_pks)

        return (multiple_choice_options, option_pks)