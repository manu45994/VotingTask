from rest_framework.response import Response
from rest_framework import status
from polls.models import Poll
from polls.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

class PollView(GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Poll.objects.all()

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return super().retrieve(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)


class PollVoteView(GenericAPIView,mixins.CreateModelMixin):
    serializer_class = CandidateElectionSerializer2
    permission_classes = (IsAuthenticated,)
    queryset = Election.objects.all()

    def post(self,request):
        serializer = CandidateElectionSerializer2(data=request.data)
        if serializer.is_valid():
            candidate = Candidate.objects.filter(id=serializer.data.get("candidate")).first()
            poll = Poll.objects.filter(id=serializer.data.get("poll")).first()
            user = User.objects.filter(id=serializer.data.get("user")).first()

            vote,created = Election.objects.get_or_create(poll=poll,user=user,candidate=candidate,vote=1)
            if created:
                vote.save()
            else:
                vote.delete()

            return Response(PollSerializer(poll).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




