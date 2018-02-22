from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MedicalList
from DjangoPython.core.Sentry import Sentry, sentry_has_access_to_feature
from django.utils.decorators import method_decorator


@method_decorator(sentry_has_access_to_feature('/ADMINISTRATOR'), name='dispatch')
class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = "ListofPharmaceuticalProducts/home.html"


@method_decorator(sentry_has_access_to_feature('/ADMINISTRATOR'), name='dispatch')
class GetMedicalListView(LoginRequiredMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):

        sortname = request.POST.get('sort[0][field]', 'name')
        sortdir = request.POST.get('sort[0][dir]', 'asc')

        if sortname.lower() == 'medicine_name':
            sortname = 'name'

        if sortdir == 'desc':
            sort = '-' + sortname.lower()
        else:
            sort = sortname.lower()

        queryset = MedicalList.objects \
            .filter(active=True, reimbursible__isnull=False, name__isnull=False) \
            .exclude(reimbursible="").exclude(reimbursible="REJECTED") \
            .order_by(sort)

        items = []

        for item in queryset:
            items.append(
                {
                    'ID': item.id,
                    'MEDICINE_NAME': item.name,
                    'COMPOSITION': item.composition,
                    'APP_DATE': item.app_date.strftime('%d/%m/%Y'),
                    'LINK': item.link,
                    'REIMBURSIBLE': item.reimbursible,
                    'COMMENTS': item.comments,
                    'USAGE': item.usage

                }
            )

        response = {
            'total': queryset.count(),
            'results': items
        }

        return JsonResponse(response, status=200, safe=False)


@method_decorator(sentry_has_access_to_feature('/ADMINISTRATOR'), name='dispatch')
class GetMedicalListDoctorView(LoginRequiredMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):

        sortname = request.POST.get('sort[0][field]', 'name')
        sortdir = request.POST.get('sort[0][dir]', 'asc')

        if sortname.lower() == 'medicine_name':
            sortname = 'name'

        if sortdir == 'desc':
            sort = '-' + sortname.lower()
        else:
            sort = sortname.lower()

        queryset = MedicalList.objects \
            .filter((Q(reimbursible__isnull=True) | Q(reimbursible="")) & Q(name__isnull=False) & Q(active=True)) \
            .order_by(sort)

        items = []

        for item in queryset:
            items.append(
                {
                    'ID': item.id,
                    'MEDICINE_NAME': item.name,
                    'COMPOSITION': item.composition,
                    'APP_DATE': item.app_date.strftime('%d/%m/%Y'),
                    'LINK': item.link,
                    'REIMBURSIBLE': item.reimbursible,
                    'COMMENTS': item.comments,
                    'USAGE': item.usage

                }
            )

        response = {
            'total': queryset.count(),
            'results': items
        }

        return JsonResponse(response, status=200, safe=False)


@method_decorator(sentry_has_access_to_feature('/ADMINISTRATOR'), name='dispatch')
class UpdateMedicalListView(LoginRequiredMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        response = {
            'ERROR': False,
            'TEXT': 'success'
        }

        _id = request.POST.get('ID', 0)

        obj = get_object_or_404(MedicalList, pk=_id)

        name = request.POST.get('MEDICINE_NAME', '')
        usage = request.POST.get('USAGE', '')
        composition = request.POST.get('COMPOSITION', '')
        comments = request.POST.get('COMMENTS', '')
        link = request.POST.get('LINK', '')
        reimbursible = request.POST.get('REIMBURSIBLE', '')

        obj.name = name
        obj.usage = usage
        obj.composition = composition
        obj.comments = comments
        obj.link = link
        obj.reimbursible = reimbursible
        obj.save()

        return JsonResponse(response, status=200, safe=False)


@method_decorator(sentry_has_access_to_feature('/ADMINISTRATOR'), name='dispatch')
class CreateMedicalListView(LoginRequiredMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        response = {
            'ERROR': False,
            'TEXT': 'success'
        }

        obj = MedicalList()

        name = request.POST.get('MEDICINE_NAME', '')
        usage = request.POST.get('USAGE', '')
        composition = request.POST.get('COMPOSITION', '')
        comments = request.POST.get('COMMENTS', '')
        link = request.POST.get('LINK', '')
        reimbursible = request.POST.get('REIMBURSIBLE', '')

        obj.name = name
        obj.usage = usage
        obj.composition = composition
        obj.comments = comments
        obj.link = link
        obj.reimbursible = reimbursible
        obj.save()

        return JsonResponse(response, status=200, safe=False)
