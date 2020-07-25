from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ballot.models import Ballot
from .serializers import BallotSerializer, VoteSerializer


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
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["POST"])
def vote(request, id):
    pass
    # serializer = VoteSerializer(data=request.data, many=False)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=201)

    # return Response(serializer.errors, status=400)
