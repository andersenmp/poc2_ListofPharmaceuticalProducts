from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from .models import MedicalList


class HomeView(TemplateView):
    template_name = "ListofPharmaceuticalProducts/home.html"


class GetMedicalListView(ListView):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        queryset = MedicalList.objects.filter(active=True)

        items = []

        for item in queryset:
            items.append(
                {
                    'id': item.id,
                    'name': item.name,
                    'composition': item.composition
                }
            )

        resultdata = {
            'total': queryset.count(),
            'results': items
        }

        return JsonResponse(resultdata, status=200, safe=False)
