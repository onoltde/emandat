from django.urls import path
from . import views

urlpatterns = [
    path('deleteprofileimage/<int:pk>', views.deleteProfileImage.as_view(), name='deleteprofileimage'),
    path('deletecompetitionfile/<int:pk>', views.deleteCompetitionFile.as_view(), name='deletecompetitionfile'),
    path('deleteuser/<int:pk>', views.deleteUser.as_view(), name='deleteuser'),
    path('deletetype/<int:pk>', views.deleteType.as_view(), name='deletetype'),
    path('deletecompetition/<int:pk>', views.deleteCompetition.as_view(), name='deletecompetition'),
    path('deletecomment/<int:pk>', views.deleteComment.as_view(), name='deletecomment'),
]