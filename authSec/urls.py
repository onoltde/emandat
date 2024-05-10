from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userView.as_view(), name = 'user'),
    path('competition/', views.competitionView.as_view(), name = 'competition'),
    path('type/', views.typeView.as_view(), name = 'type'),
    path('upvotecompetition/', views.upVoteCompetition.as_view(), name='upvotecompetition'),
    path('downvotecompetition/', views.downVoteCompetition.as_view(), name='downvotecompetition'),
    path('upvotecomment/', views.upVoteComment.as_view(), name='upvotecomment'),
    path('downvotecomment/', views.downVoteComment.as_view(), name='downvotecomment'),
]