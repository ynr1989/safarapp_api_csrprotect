from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="SAFFAR API DOCUMENTATION")

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include('users.urls')),
]
