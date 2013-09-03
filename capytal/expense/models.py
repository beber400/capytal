# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Expense(models.Model):
    """The Expense class holds information about who spend what and when"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='+', verbose_name=u'émetteur')
    amount = models.FloatField(validators=[MinValueValidator(0)],
        verbose_name=u'montant')
    recipients = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='+', verbose_name=u'bénéficiaires')
    name = models.CharField(max_length=100, verbose_name=u'nom')

    def __unicode__(self):
        return u'%s - %d€' % (self.name, self.amount)