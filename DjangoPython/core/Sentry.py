from main.models import SentryModel
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse


class Sentry:
    def __init__(self, user):
        self.user = user
        self.sentryFeatures = SentryModel.objects.filter(login=user.username)
        if self.sentryFeatures.exists():
            self.first_name = self.sentryFeatures.first().first_name
            self.last_name = self.sentryFeatures.first().last_name
            self.email = self.sentryFeatures.first().email
        else:
            self.first_name = user.username
            self.last_name = "Not in Sentry"
            self.email = "email@not.registed.com"

    def get_total_rows(self):
        return self.sentryFeatures.count()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def has_access_to_feature(self, feature):
        if '|' in feature:
            for x in feature.split('|'):
                if self.sentryFeatures.filter(feature__contains=x).exists():
                    return True
        else:
            return self.sentryFeatures.filter(feature__contains=feature).exists()
        return False


def sentry_has_access_to_feature(feature):
    def real_decorator(function):
        def wrap(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse('main:home'))
            sentry = Sentry(user=request.user)
            if sentry.has_access_to_feature(feature):
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied

        wrap.__doc__ = function.__doc__
        wrap.__name__ = function.__name__
        return wrap

    return real_decorator
