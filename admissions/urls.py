from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('admissions/', views.admissions_list, name='admissionsList'),
    path('admissionscreate/', csrf_exempt(views.admissions_create), name='admissionsCreate'),
]