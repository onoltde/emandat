from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from authSec.serializers import *
from .models import *
from datetime import timezone
import os

class deleteProfileImage(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            if user.profile.image:
                os.remove(user.profile.image.path)
            
            user.profile.image = None
            return Response({'message': 'Profile image deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteCompetitionFile(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request, pk):
        try:
            competition = get_object_or_404(Competitions, pk=pk)

            if competition.file:
                os.remove(competition.file.path)
            
            competition.file = None

            return Response({'message': 'Attached file deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class deleteUser(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            user.delete()

            return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteCompetition(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request, pk):
        try:
            competition = get_object_or_404(competition, pk=pk)
            competition.delete()

            return Response({'message': 'Competition deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteType(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request, pk):
        try:
            type = get_object_or_404(Types, pk=pk)
            type.delete()

            return Response({'message': 'Type deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class deleteComment(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request, pk):
        try:
            comment = get_object_or_404(Comments, pk=pk)
            comment.delete()

            return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)