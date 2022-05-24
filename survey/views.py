from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import SurveyCollectorSerializers
from django.db import transaction
from .models import SurveyCollector
from django.contrib.auth.models import User

class SurveyCollectorList(APIView):
    def post(self, request, format=None):
        survey = request.data['survey']
        users = request.data['users']
        all_data = []
        existing_user = []
        for user in users:
            if SurveyCollector.objects.filter(survey = survey, user = user['id']).exists():
                existing_user.append( user['id'])
            else:
                data = {"survey": survey, "user":user['id']}
                all_data.append(data)
        
        if existing_user:
            return Response({"message": f"User Id {existing_user} is already exist this survey"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer = SurveyCollectorSerializers(data=all_data, many = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    
