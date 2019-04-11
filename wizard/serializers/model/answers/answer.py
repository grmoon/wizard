from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.answers.file import FileAnswer, FileAnswerSerializer
from wizard.serializers.model.answers.json import JSONAnswer, JSONAnswerSerializer

from wizard.models import Answer

class AnswerSerializer(GenericSerializer):
    SERIALIZERS = {
        FileAnswer: FileAnswerSerializer,
        JSONAnswer: JSONAnswerSerializer,
    }