from django.conf.urls import url
from patients import views

urlpatterns = [
    url(r'^api/find', views.find_patient, name='Find_Patient'),
    url(r'^api/patientlist', views.patient_list),
    url(r'^api/createPatient', views.createPatient)
]