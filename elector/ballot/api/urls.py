from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='ballot-api-create'),
    path('delete/<int:id>/', views.delete, name='ballot-api-delete'),
    path('<int:id>/', views.detail, name='ballot-api-detail'),
    path('vote/', views.vote, name='ballot-api-vote'),
]
