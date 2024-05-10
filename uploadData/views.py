from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.views import APIView
from authSec.tokens import MyTokenObtainPairSerializer
from authSec.serializers import *
from .models import *
from datetime import timezone
import os

class addRegisteredCompetition(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        try:
            data = request.data
            pk1 = data['profile']
            pk2 = data['competition']
            profile = get_object_or_404(Profiles, pk=pk1)
            competition = get_object_or_404(Competitions, pk=pk2)
            profile.registeredcompetitions.add(competition)
            
            return Response({'message': 'Competition added successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class updateBio(APIView):
    permission_classes = (permissions.AllowAny, )
    def patch(self, request):
        try:
            data = request.data
            pk = data['profile']
            bio = data['bio']
            profile = get_object_or_404(Profiles, pk=pk)
            profile.bio = bio
            profile.save()
            return Response({'message': 'Bio Updated successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class uploadPicture(APIView):
    permission_classes = (permissions.AllowAny, )
    def patch(self, request):
        try:
            data = request.data
            pk = data['profile']
            image = data['image']
            profile = get_object_or_404(Profiles, pk=pk)
            if profile.image:
                os.remove(profile.image)
            profile.image = image
            profile.save()
            return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)