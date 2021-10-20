from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE,related_name="candidates")
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Election(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE,related_name="election")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="election")
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name="election")
    vote = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.candidate.poll} candidate {self.candidate.name}"
        
