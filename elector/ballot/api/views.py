from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from settings_json import get_setting
from ballot.models import Ballot, Voter, Vote
from .serializers import BallotSerializer, VoterSerializer
from secrets import token_urlsafe

@api_view(["GET"])
def detail(request, id):
    ballot = get_object_or_404(Ballot, id=id)
    serializer = BallotSerializer(ballot, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete(request, id):
    ballot = get_object_or_404(Ballot, id=id)
    ballot.delete()
    return Response()


@api_view(["POST"])
def create(request):
    serializer = BallotSerializer(data=request.data, many=False)
    voter_list = list(set(request.data.get("voter_list")))
    if not voter_list:
        return Response({"voter_list": ["This field is required."]}, status=400)
    if serializer.is_valid():
        ballot = serializer.save()
        for email in voter_list:
            token = token_urlsafe(16)
            voter = Voter(ballot=ballot, token=token)
            voter.save()
            send_mail("subject", token, get_setting("EMAIL"), [email], fail_silently=True)
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def vote(request):
    serializer = VoterSerializer(data=request.data, many=False)
    if serializer.is_valid():
        ballot = serializer.validated_data["ballot"]
        token = serializer.validated_data["token"]
        options = request.data.get("options")
        if token in [vote.voter.token for vote in ballot.votes]:
            return Response({"detail": "you already voted"}, status=403)
        elif timezone.now() >= ballot.deadline:
            return Response({"detail": "can not vote past deadline"}, status=403)
        elif not options:
            return Response({"options": ["This field is required."]}, status=400)
        else:
            update_votes(options, ballot)
            vote = Vote(voter=Voter.objects.get(token=token), ballot=ballot)
            vote.save()
            return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)




def update_votes(options, ballot):
    questions = ballot.questions
    question_numbers = {question.question_number for question in questions}
    keys = {int(elem) for elem in options.keys()}
    if len(keys) == len(question_numbers) and set(keys) == question_numbers:
        for question_number, option in options.items():
            question = questions.get(question_number=question_number)
            option_model = question.options.get(option_number=option)
            if option_model:
                option_model.votes += 1
                option_model.save()
