from django.db import models
from django.utils import timezone


class Ballot(models.Model):
    title = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"#{self.pk} {self.title}"

    @property
    def questions(self):
        return self.question_set.all()


class Question(models.Model):
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return f"#{self.pk} {self.question_text}"

    @property
    def options(self):
        return self.option_set.all()


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"#{self.pk} {self.option_text}"


class Vote(models.Model):
    voter_id = models.CharField(max_length=250)
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.voter_id} voted in {self.ballot}"