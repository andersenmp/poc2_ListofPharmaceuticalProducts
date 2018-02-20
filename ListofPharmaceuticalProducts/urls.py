from django.urls import path
from .views import *

app_name="ListofPharmaceuticalProducts"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('GetMedicalList/', GetMedicalListView.as_view(), name='GetMedicalListView'),
]
