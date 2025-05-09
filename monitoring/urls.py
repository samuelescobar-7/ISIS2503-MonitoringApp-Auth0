from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('measurements.urls')),
    path('', include('variables.urls')),
    path('', include('admissions.urls')),
]

