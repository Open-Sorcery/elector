from rest_framework.serializers import ModelSerializer
from ballot.models import Ballot, Question, Option


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = [
            # 'id',
            "option_text",
            "votes",
        ]


class QuestionSerializer(ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            # 'id',
            "question_text",
            "options",
        ]


class BallotSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Ballot
        fields = ["id", "title", "date_created", "questions"]
