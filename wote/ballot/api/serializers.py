from rest_framework.serializers import ModelSerializer
from ballot.models import Ballot, Question, Option, Vote


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
        fields = [
            "id", 
            "title",
            "date_created",
            "questions"
        ]
    
    def create(self, validated_data):
        questions = validated_data.pop("questions")
        ballot = Ballot.objects.create(**validated_data)
        for question in questions:
            options = question.pop("options")
            question = Question.objects.create(**question, ballot=ballot)
            for option in options:
                Option.objects.create(**option, question=question)

        return ballot

class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            # "id", 
            "voter_id",
            "ballot",
            "date_created"
        ]
    
    def create(self, validated_data):
        pass