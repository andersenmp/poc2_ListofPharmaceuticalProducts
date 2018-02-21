from django.test import TestCase
from ListofPharmaceuticalProducts.models import *


# Tests for models

class TestContractorModel(TestCase):
    def setUp(self):
        self.user = User(username='test')
        self.user.save()

    def test_medicine_contractor(self):
        mll = MedicalList()
        mll.name = 'Name'
        mll.composition = 'composition'
        mll.id = 1
        mll.comments = 'commnets'
        mll.link = 'casa'
        mll.save()

    def test_medicine_return(self):
        ml = MedicalList(name="Name")
        print(ml)



