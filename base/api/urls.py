from django.urls import path,include

urlpatterns = [ 
    path("poll/",include("polls.urls")),
    path("auth/",include("authorization.urls"))
]