from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^api/patient/findPatient/(?P<pk>[0-9]+)/$', views.find_patient, name='Find_Patient'),
    url(r'^api/patient/patientlist/$', views.patient_list, name='Get_ALL_PatientList'),
    url(r'^api/patient/register/$', views.register, name='Register_Patient'),
    url(r'^api/patient/getPatient/', views.getPatientDetails, name = 'Get_Patient_details'),
    url(r'^api/patient/login/$', views.login, name='Patient_login')
]