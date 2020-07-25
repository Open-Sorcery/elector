from django.db import models
from django.utils import timezone


class Ballot(models.Model):
    title = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=timezone.now)
    deadline = models.DateTimeField(null=False)

    def __str__(self):
        return f"#{self.pk} {self.title}"

    @property
    def questions(self):
        return self.question_set.all()

    @property
    def voters(self):
        return self.voter_set.all()

    @property
    def votes(self):
        return self.vote_set.all()



class Question(models.Model):
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)
    question_number = models.IntegerField(null=True)

    def __str__(self):
        return f"#{self.pk} {self.question_text}"

    @property
    def options(self):
        return self.option_set.all()


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    option_number = models.IntegerField(null=True)

    def __str__(self):
        return f"#{self.pk} {self.option_text}"


class Voter(models.Model):
    token = models.CharField(max_length=250)
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.token} participates in {self.ballot}"

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return f"{self.voter.token} voted in {self.voter.ballot}"
