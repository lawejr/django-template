from uuid import uuid4
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext as _


class Uided(models.Model):
    """
    Primary Uided
    """
    UID_PREFIX = 'OBJ'
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    @cached_property
    def suid(self) -> str:
        """
        String representation of UID
        """
        return "{{{0}-{1}}}".format(self.UID_PREFIX, self.uid).lower()

    def __str__(self):
        return self.suid

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_('Created'),
        db_index=True
    )
    updated = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_('Updated'),
        db_index=True
    )

    class Meta:
        abstract = True
