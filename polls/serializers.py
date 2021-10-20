from django.db.models import fields
from rest_framework import serializers
from .models import *

class PollSerializer(serializers.ModelSerializer):
    candidate = serializers.SerializerMethodField()
    def get_candidate(self,poll):
        candidates = poll.candidates.all()
        serializer = CandidateSerializer(candidates,many=True)
        return serializer.data

    class Meta:
        model = Poll
        fields = ["id","name","candidate"]

class CandidateSerializer(serializers.ModelSerializer):

    vote = serializers.SerializerMethodField()
    def get_vote(self,candidate):
        return candidate.election.count()

    class Meta:
        model = Candidate
        fields = ["id","name","vote"]

class CandidateElectionSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    def get_name(self,election):
        return election.candidate.name

    class Meta:
        model = Election
        fields = ["id","name","vote"]

class CandidateElectionSerializer2(serializers.ModelSerializer):
    poll = serializers.CharField(max_length=150)
    candidate = serializers.CharField(max_length=150)
    class Meta:
        model = Election
        fields = ["poll","user","candidate"]