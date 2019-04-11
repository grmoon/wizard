from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.questions.file import FileQuestion, FileQuestionSerializer
from wizard.serializers.model.questions.json import JSONQuestion, JSONQuestionSerializer

from wizard.models import Question, Trigger

class QuestionSerializer(GenericSerializer):
    SERIALIZERS = {
        FileQuestion: FileQuestionSerializer,
        JSONQuestion: JSONQuestionSerializer,
    }