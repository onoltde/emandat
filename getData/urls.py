from django.urls import path
from . import views

urlpatterns = [
    path('getcompetitionsbyuser/<int:pk>/', views.getCompetitionsByUser.as_view(), name='getcompetitionsbyuser'),
    path('getcompetitionsbytype/<int:pk>/', views.getCompetitionsByType.as_view(), name='getcompetitionsbytype'),
    path('getcommentsbycompetition/<int:pk>/', views.getCommentsByCompetition.as_view(), name='getcommentsbycompetition'),
    path('getcommentsbyuser/<int:pk>/', views.getCommentsByUser.as_view(), name='getcommentsbyuser'),
    path('getprofilebyuser/<int:pk>/', views.getProfileByUser.as_view(), name='getprofilebyuser'),
    path('getuserbyid/<int:pk>/', views.getUserById.as_view(), name='getuserbyid'),
    path('getcompetitionbyid/<int:pk>/', views.getCompetitionById.as_view(), name='getcompetitionbyid'),
    path('getcommentbyid/<int:pk>/', views.getCommentById.as_view(), name='getcommentbyid'),
    path('getprofilebyid/<int:pk>/', views.getProfileById.as_view(), name='getprofilebyid'),
    path('gettypebyid/<int:pk>/', views.getTypeById.as_view(), name='gettypebyid'),
    path('getcompetitions/', views.getCompetitions.as_view(), name='getcompetitions'),
    path('getusers/', views.getUsers.as_view(), name='getusers'),
    path('gettypes/', views.getTypes.as_view(), name='gettypes'),
]
