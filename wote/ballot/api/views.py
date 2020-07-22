from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ballot.models import Ballot
from .serializers import BallotSerializer


@api_view(["GET"])
def detail(request, id):
    ballot = get_object_or_404(Ballot, id=id)
    serializer = BallotSerializer(ballot, many=False)
    return Response(serializer.data)
