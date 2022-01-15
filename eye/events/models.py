from datetime import datetime

import pytz
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.utils import check_structure


class Session(models.Model):
    """Class for modeling sessions"""
    application = models.ForeignKey(User, verbose_name=_('Application'), on_delete=models.PROTECT)
    uuid = models.UUIDField(verbose_name=_('Session UUID'))

    def __str__(self):
        """String representation"""
        return self.__unicode__()

    def __unicode__(self):
        """Unicode representation"""
        return f'{self.application.name}-{self.uuid}'

    class Meta:
        """Meta Class of Session class"""
        ordering = ('application__first_name', 'uuid')
        verbose_name = _('Session')
        verbose_name_plural = _('Sessions')


class EventType(models.Model):
    """Class for modeling event type"""
    category = models.CharField(max_length=50, verbose_name=_('Category'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    structure = models.JSONField(verbose_name=_('Example of payload'), null=True, blank=True)

    def __str__(self):
        """String representation"""
        return self.__unicode__()

    def __unicode__(self):
        """Unicode representation"""
        return f'{self.category}-{self.name}'

    def validate_payload(self, payload):
        """Validate payload structure"""
        return check_structure(self.structure, payload)

    class Meta:
        """Meta Class of Event class"""
        verbose_name = _('Event Type')
        verbose_name_plural = _('Event Types')
        unique_together = ['category', 'name']


def no_future(value):
    now = datetime.utcnow()
    if value > now.replace(tzinfo=pytz.UTC):
        raise ValidationError('timestamp cannot be in the future.')


class Event(models.Model):
    """Class for modeling events"""
    session = models.ForeignKey(Session, verbose_name=_('Session UUID'), on_delete=models.PROTECT)
    category = models.CharField(max_length=50, verbose_name=_('Category'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    data = models.JSONField(verbose_name=_('Payload of data'))
    timestamp = models.DateTimeField(verbose_name=_('Timestamp'), validators=[no_future])

    def __str__(self):
        """String representation"""
        return self.__unicode__()

    def __unicode__(self):
        """Unicode representation"""
        return f'{self.session}-{self.timestamp}'

    class Meta:
        """Meta Class of Event class"""
        ordering = ('timestamp',)
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
