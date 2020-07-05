from django.conf.urls import url, include

urlpatterns = [
    #   url(r'^api/auth/', include('login.urls')),
    url(r'^', include('patients.urls')),
]
