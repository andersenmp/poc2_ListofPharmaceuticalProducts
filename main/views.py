from django.views.generic import TemplateView

class HomeView(TemplateView):
    #logger.info("HomeView")
    template_name = "main/home.html"