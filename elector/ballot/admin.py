from django.contrib import admin
from .models import Ballot, Question, Option, Voter, Vote

# Register your models here.
admin.site.register(Ballot)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Voter)
admin.site.register(Vote)