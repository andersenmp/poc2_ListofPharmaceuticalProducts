from django.urls import path
from .views import *

app_name="ListofPharmaceuticalProducts"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('GetMedicalList/', GetMedicalListView.as_view(), name='GetMedicalListView'),
    path('UpdateMedicalList/', UpdateMedicalListView.as_view(), name='UpdateMedicalListView'),
    path('CreateMedicalList/', CreateMedicalListView.as_view(), name='CreateMedicalListView'),
    path('GetMedicalListDoctor/', GetMedicalListDoctorView.as_view(), name='GetMedicalListDoctorView'),
]
