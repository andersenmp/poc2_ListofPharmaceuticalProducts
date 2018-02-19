from django.db import models


class AuditTrail(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and modified fields.
    """

    active = models.BooleanField(default=True)
    modified = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
            abstract = True



