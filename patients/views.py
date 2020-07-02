from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def patient_list(request):
    if request.method == 'GET':
        tutorials = Patient.objects.all()
        tutorials_serializer = PatientSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['POST'])
def createPatient(request):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = PatientSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return JsonResponse({'message': 'Patient doesnt exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        patient_serializer = PatientSerializer(patient)
        return JsonResponse(patient_serializer.data)

