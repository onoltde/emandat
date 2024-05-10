from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from authSec.serializers import *
from .models import *
from datetime import timezone
import os

class getCompetitionsByUser(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            competitions = user.competitions_set.all()
            serializer = CompetitionSerializer(competitions, many=True)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getCompetitionsByType(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            type = get_object_or_404(Types, pk=pk)
            competitions = type.competitions_set.all()
            serializer = CompetitionSerializer(competitions, many=True)
            return Response({'context' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getCommentsByCompetition(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            competition = get_object_or_404(Competitions, pk=pk)
            comments = competition.comments_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response({'context' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getCommentsByUser(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            comments = user.comments_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response({'context' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getProfileByUser(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            serializer = ProfileSerializer(user.profile)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getUserById(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getCompetitionById(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            competition = get_object_or_404(Competitions, pk=pk)
            serializer = CompetitionSerializer(competition)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
    
class getTypeById(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            type = get_object_or_404(Types, pk=pk)
            serializer = TypeSerializer(type)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class getProfileById(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            profile = get_object_or_404(Profiles, pk=pk)
            serializer = ProfileSerializer(profile)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getCommentById(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, pk):
        try:
            comment = get_object_or_404(Comments, pk=pk)
            serializer = CommentSerializer(comment)
            return Response({'context': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class getUsers(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class getTypes(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request):
        types = Types.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)

class getCompetitions(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request):
        competitions = Competitions.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)