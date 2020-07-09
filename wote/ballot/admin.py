from django.contrib import admin
from .models import Ballot, Question, Option

# Register your models here.
admin.site.register(Ballot)
admin.site.register(Question)
admin.site.register(Option)