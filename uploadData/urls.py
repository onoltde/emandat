from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('addresigterecompetition/', views.addRegisteredCompetition.as_view(), name = 'addregisteredcompetition'),
    path('updatebio/', views.updateBio.as_view(), name = 'updatebio'),
    path('uploadpicture/', views.uploadPicture.as_view(), name = 'uploadpicture'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)