from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.conf import settings as conf_settings
from .models import Patient, UserToken
from patients.serializers import PatientSerializer, UserTokenSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from login.decorators import token_authentication_required

import datetime
import jwt

SECRET_KEY = conf_settings.SECRET_KEY
JWT_ACCESS_TOKEN_LIFE_SPAN = conf_settings.JWT_ACCESS_TOKEN_LIFE_SPAN
JWT_REFRESH_TOKEN_LIFE_SPAN = conf_settings.JWT_REFRESH_TOKEN_LIFE_SPAN


@api_view(['GET'])
@csrf_exempt
def patient_list(request):
    if request.method == 'GET':
        tutorials = Patient.objects.all()
        tutorials_serializer = PatientSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['POST'])
@csrf_exempt
def register(request):
    if request.method == 'POST':
        serializer_data = JSONParser().parse(request)
        serializer = PatientSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def find_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return JsonResponse({'message': 'Patient doesnt exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        patient_serializer = PatientSerializer(patient)
        return JsonResponse(patient_serializer.data)


@api_view(['POST'])
@csrf_exempt
def login(request):
    if not request.data:
        return JsonResponse({'message': "Please provide username/password"}, status=status.HTTP_400_BAD_REQUEST)
    email = request.data['email']
    password = request.data['password']

    try:
        patient = Patient.objects.get(email=email)
        count_user_id = UserToken.objects.filter(user_id=patient.id).count()
    except Patient.DoesNotExist:
        return JsonResponse({'message': "Invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)

    print("password", password, "patient.password", patient.password)

    if patient and (password == patient.password):
        payload_access_token = getPayload(patient.id, JWT_ACCESS_TOKEN_LIFE_SPAN)
        payload_refresh_token = getPayload(
            patient.id, JWT_REFRESH_TOKEN_LIFE_SPAN)
        jwt_access_token = jwt.encode(
            payload_access_token, SECRET_KEY, algorithm='HS256')
        jwt_refresh_token = jwt.encode(
            payload_refresh_token, SECRET_KEY, algorithm='HS256')

        if int(count_user_id) > 0:
            UserToken.objects.filter(user_id=patient.id).update(
                access_token=jwt_access_token, refresh_token=jwt_refresh_token)
        else:
            user_token_instance = UserToken(
                access_token=jwt_access_token, refresh_token=jwt_refresh_token, user_id=patient.id)
            user_token_instance.save()

        userToken = UserToken.objects.get(user_id=patient.id)
        serialzer_utoken = UserTokenSerializer(userToken)
        return JsonResponse(serialzer_utoken.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@token_authentication_required
def getPatientDetails(request):
    email = request.data['email']
    patient = Patient.objects.get(email=email)
    patient_serializer = PatientSerializer(patient)
    return JsonResponse(patient_serializer.data, status=status.HTTP_200_OK)


def getPayload(info, timeDelta):
    payload = {
        'info': info,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=timeDelta)
    }
    return payload
