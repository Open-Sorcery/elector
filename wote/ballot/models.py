from django.db import models
from django.utils import timezone


class Ballot(models.Model):
    title = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"#{self.pk} {self.title}"


class Question(models.Model):
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return f"#{self.pk} {self.question_text}"


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"#{self.pk} {self.choice_text}"
