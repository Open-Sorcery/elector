from django.shortcuts import render


def home(request):
    return render(request, "ballot/home.html")


def delete(request):
    return render(request, "ballot/home.html")


def create(request):
    return render(request, "ballot/create.html")


def detail(request, id):
    return render(request, "ballot/home.html")


def vote(request, id):
    return render(request, "ballot/home.html")

