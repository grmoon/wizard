from collections import namedtuple

from wizard.models import (
    CheckboxField,
    CheckboxOption,
    Field,
    FileAnswer,
    FileField,
    FileQuestion,
    JSONAnswer,
    JSONQuestion,
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
    Upload,
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
    UploadSerializer,
)

MultipleChoiceFieldMapping = namedtuple('FieldMapping', ('field_class', 'option_class'))
QuestionAnswerMapping = namedtuple('QuestionMapping', ('question_class', 'answer_class'))

class WizardStepResponseBuilder(object):
    FIELD_CLASSES = (
        CheckboxField,
        RadioButtonField,
        SelectField,
        TextField,
        FileField,
    )

    ANSWER_CLASSES = (
        FileAnswer,
        JSONAnswer,
    )

    QUESTION_CLASSES = (
        FileQuestion,
        JSONQuestion,
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

        # From here down, there are multiple subclasses for every class
        # e.g. Answer => JSONAnswer & FileAnswer, Question => JSONQuestion & FileQuestion
        questions = cls._get_questions_for_section_questions(section_questions)
        answers = cls._get_answers_from_questions(user, questions)
        triggers = cls._get_triggers_from_questions(questions)
        uploads = cls._get_uploads_from_answers(answers)

        field_pks = [question.field_id for question in questions]
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
            'uploads': UploadSerializer(uploads, many=True).data,
        }

    @staticmethod
    def _get_wizard_step_for_wizard(wizard_id, step_num):
        return WizardStep.objects\
            .select_related('step')\
            .prefetch_related('step__sections')\
            .prefetch_related('step__sections__questions')\
            .filter(wizard_id=wizard_id)\
            .order_by('position')[step_num - 1]

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

    @classmethod
    def _get_questions_for_section_questions(cls, section_questions):
        question_pks = section_questions.values_list('question_id', flat=True)

        questions_from_section_questions = cls._get_questions_from_pks(question_pks)
        questions_from_triggers = cls._get_questions_for_question_triggers(questions_from_section_questions)

        return list(questions_from_section_questions) + list(questions_from_triggers)

    @classmethod
    def _get_questions_from_pks(cls, question_pks):
        questions = []

        for question_class in cls.QUESTION_CLASSES:
            _questions = question_class.objects\
                .filter(pk__in=question_pks)\
                .all()

            questions += list(_questions)

        return questions

    @classmethod
    def _get_questions_for_question_triggers(cls, questions):
        from_question_pks = [question.pk for question in questions]

        to_question_pks = Trigger.objects\
            .filter(from_question__pk__in=from_question_pks)\
            .values_list('to_question', flat=True)

        to_questions = cls._get_questions_from_pks(to_question_pks)

        if len(to_questions) > 0:
            questions = to_questions + cls._get_questions_for_question_triggers(to_questions)
        else:
            questions = to_questions

        return questions

    @staticmethod
    def _get_triggers_from_questions(questions):
        question_pks = [question.pk for question in questions]

        return Trigger.objects.filter(from_question__pk__in=question_pks).all()

    @classmethod
    def _get_fields_from_pks(cls, field_pks):
        fields = list()

        for field_class in cls.FIELD_CLASSES:
            fields += list(field_class.objects.filter(pk__in=field_pks))

        return fields

    @classmethod
    def _get_answers_from_questions(cls, user, questions):
        answers = []
        question_pks = [question.pk for question in questions]

        for answer_class in cls.ANSWER_CLASSES:
            answers += list(answer_class.objects.filter(user=user, question__pk__in=question_pks))

        return answers

    @staticmethod
    def _get_uploads_from_answers(answers):
        answer_pks = [answer.pk for answer in answers]

        return Upload.objects.filter(answer__pk__in=answer_pks).all()

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