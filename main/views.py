from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from DjangoPython.core.Sentry import Sentry


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        sentry = Sentry(user=self.request.user)
        context['sentry_count'] = sentry.get_total_rows()
        context['menu_ListofPharmaceuticalProducts'] = sentry.has_access_to_feature('/ADMINISTRATOR')
        return context


