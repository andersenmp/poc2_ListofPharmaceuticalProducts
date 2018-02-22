from django.test import TestCase
from ListofPharmaceuticalProducts.models import *


# reload('ListofPharmaceuticalProducts.models.*')

# Tests for models

class TestContractorModel(TestCase):
    def setUp(self):
        self.user = User(username='test')
        self.user.save()

    def test_medicine_list_model(self):
        mll = MedicalList()
        mll.name = 'Name'
        mll.composition = 'composition'
        mll.comments = 'commnets'
        mll.link = 'casa'
        mll.save()
        obj = MedicalList.objects.get(pk=mll.pk)
        self.assertEqual(obj.name, mll.name)

    def test_medicine_return(self):
        ml = MedicalList(name="Name")
        print(ml)



