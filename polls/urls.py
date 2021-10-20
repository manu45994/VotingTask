from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [ 
    path("list/",PollView.as_view(),name="poll-list"),
    path("<str:pk>/",PollView.as_view(),name="poll-detail"),
    path("vote/", PollVoteView.as_view(),name="poll-vote"),
]