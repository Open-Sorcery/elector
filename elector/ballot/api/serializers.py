from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ballot.models import Ballot, Question, Option, Voter


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = [
            # 'id',
            "option_number",
            "option_text",
            "votes",
        ]


class QuestionSerializer(ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            # 'id',
            "question_number",
            "question_text",
            "options",
        ]


class BallotSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Ballot
        fields = [
            "id", 
            "title",
            "date_created",
            "deadline",
            "questions"
        ]
    
    def create(self, validated_data):
        questions = validated_data.pop("questions")
        ballot = Ballot.objects.create(**validated_data)
        for question_number, question in enumerate(questions):
            options = question.pop("options")
            question["question_number"] = question_number
            question = Question.objects.create(**question, ballot=ballot)
            for option_number, option in enumerate(options):
                option.pop("votes", None)
                option["option_number"] = option_number
                Option.objects.create(**option, question=question)

        return ballot

class VoterSerializer(ModelSerializer):
    class Meta:
        model = Voter
        fields = [
            # "id", 
            "token",
            "ballot"
        ]
    