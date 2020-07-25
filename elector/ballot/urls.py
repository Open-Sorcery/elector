from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="ballot-home"),
    path("create/", views.create, name="ballot-create"),
    path("delete/", views.delete, name="ballot-delete"),
    path("<int:id>/", views.detail, name="ballot-detail"),
    path("<int:id>/vote/", views.vote, name="ballot-vote"),
    path("api/", include("ballot.api.urls")),
]
