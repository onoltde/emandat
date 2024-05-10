from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.views import APIView
from .tokens import MyTokenObtainPairSerializer
from .serializers import *
from .models import *
from django.utils import timezone
import os
from django.db import IntegrityError

User = get_user_model()

class userView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        try:
            data = request.data
            
            firstname = data['firstname']
            lastname = data['lastname']
            phonenumber = data['phonenumber']
            birthday = data['birthday']
            email = data['email']
            password = data['password']
            confirmpassword = data['confirmpassword']
            if password != confirmpassword:
                return Response({'error': 'Passwords must match'}, status=status.HTTP_400_BAD_REQUEST)
            if len(password) < 8 or len(password) > 20:
                return Response({'error' : 'Password length must be between 8 and 20'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(firstname=firstname, lastname=lastname, phonenumber=phonenumber, birthday=birthday, email=email)
            user.set_password(password)

            profile = Profiles.objects.create(user=user)

            user.save()
            
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request):
        try:
            data = request.data
            
            firstname = data['firstname']
            lastname = data['lastname']
            phonenumber = data['phonenumber']
            birthday = data['birthday']
            email = data['email']
            pk = data['user']
            user = get_object_or_404(User, pk=pk)
            user.firstname = firstname
            user.lastname = lastname
            user.phonenumber = phonenumber
            user.birthday = birthday
            user.email = email
            user.save()
            
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
        
class typeView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        try:
            data = request.data

            name = data['name']
            Types.objects.create(name=name)
            return Response({'message': 'Type added successfully'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request):
        try:
            data = request.data

            name = data['name']
            pk = data['type']
            type = get_object_or_404(Types, pk=pk)
            type.name = name
            type.save()
            return Response({'message': 'Type updated successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class competitionView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        try:
            data = request.data

            name = data['name']
            startdate = data['startdate']
            enddate = data['enddate']
            description = data['description']
            organizer = get_object_or_404(User, pk=data['organizer'])
            type = data['type']
            file = data.get('file')
            uploadeddate = timezone.now()

            competition = Competitions.objects.create(
                name=name, 
                startdate=startdate, 
                enddate=enddate, 
                description=description, 
                organizer=organizer, 
                uploadeddate=uploadeddate, 
                file=file
            )

            for pk in type:
                competition.type.add(get_object_or_404(Types, pk=pk))

            return Response({'message': 'Competition added successfully'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request):
        try:
            data = request.data
            
            name = data['name']
            startdate = data['startdate']
            enddate = data['enddate']
            description = data['description']
            organizer = get_object_or_404(User, pk=data['organizer'])
            type = data['type']
            file = data['file']
            pk = data['competition']

            competition = get_object_or_404(Competitions, pk=pk)
            competition.name = name
            competition.startdate = startdate
            competition.enddate = enddate
            competition.description = description
            competition.organizer = organizer

            if competition.file:
                os.remove(competition.file.path)
            
            competition.file = file

            competition.save()

            
            competition.type.clear()
            for pk in type:
                competition.type.add(get_object_or_404(Types, pk=pk))
            
            return Response({'message': 'Competition updated successfully'}, status=status.HTTP_200_OK)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class upVoteCompetition(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            pk1 = data['user']
            pk2 = data['competition']

            user = get_object_or_404(User, pk=pk1)
            competition = get_object_or_404(Competitions, pk=pk2)

            if competition.upvote.filter(pk=pk1).exists():
                competition.delta -= 1
                competition.upvote.remove(user)
            elif competition.downvote.filter(pk=pk1).exists():
                competition.delta += 2
                competition.downvote.remove(user)
                competition.upvote.add(user)
            else:
                competition.delta += 1
                competition.upvote.add(user)

            competition.save()

            return Response({'message': 'Upvoted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class downVoteCompetition(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        try:
            data = request.data
            pk1 = data['user']
            pk2 = data['competition']

            user = get_object_or_404(User, pk=pk1)
            competition = get_object_or_404(Competitions, pk=pk2)

            if competition.downvote.filter(pk=pk1).exists():
                competition.delta += 1
                competition.downvote.remove(user)
            elif competition.upvote.filter(pk=pk1).exists():
                competition.delta -= 2
                competition.upvote.remove(user)
                competition.downvote.add(user)
            else:
                competition.delta -= 1
                competition.downvote.add(user)
            
            competition.save()

            return Response({'message': 'Downvoted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class upVoteComment(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            pk1 = data['user']
            pk2 = data['comment']

            user = get_object_or_404(User, pk=pk1)
            comment = get_object_or_404(Comments, pk=pk2)

            if comment.upvote.filter(pk=pk1).exists():
                comment.delta -= 1
                comment.upvote.remove(user)
            elif comment.downvote.filter(pk=pk1).exists():
                comment.delta += 2
                comment.downvote.remove(user)
                comment.upvote.add(user)
            else:
                comment.delta += 1
                comment.upvote.add(user)

            comment.save()

            return Response({'message': 'Upvoted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class downVoteComment(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        try:
            data = request.data
            pk1 = data['user']
            pk2 = data['comment']

            user = get_object_or_404(User, pk=pk1)
            comment = get_object_or_404(Comments, pk=pk2)

            if comment.downvote.filter(pk=pk1).exists():
                comment.delta += 1
                comment.downvote.remove(user)
            elif comment.upvote.filter(pk=pk1).exists():
                comment.delta -= 2
                comment.upvote.remove(user)
                comment.downvote.add(user)
            else:
                comment.delta -= 1
                comment.downvote.add(user)
            
            comment.save()

            return Response({'message': 'Downvoted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)