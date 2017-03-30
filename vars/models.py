from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def validate_uppercase(value):
    if value != value.upper():
        raise ValidationError('Value needs to be upper case',
                              code='invalid')


class Var(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'is_staff': False})
    name = models.CharField(max_length=255, validators=[validate_uppercase])
    value = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("owner", "name")
