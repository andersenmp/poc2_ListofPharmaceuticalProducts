from django.contrib.auth.models import User
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated, cas_user_logout
from DjangoPython.core.Sentry import Sentry


@receiver(cas_user_authenticated, dispatch_uid="unique")
def user_authenticated_(sender, user, created, attributes, ticket, service, request,**kwargs):
    sentry = Sentry(user)
    obj = User.objects.get(username=user)
    obj.first_name = sentry.get_first_name()
    obj.last_name = sentry.get_last_name()
    obj.email = sentry.get_email()
    obj.save()


@receiver(cas_user_logout, dispatch_uid="unique")
def user_logout_(sender, user, session, ticket,**kwargs):
    pass
