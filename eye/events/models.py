from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    """Class for modeling applications"""
    name = models.CharField(max_length=50, verbose_name=_('Application Name'))
    host = models.URLField(verbose_name=_('Application Host'))

    def __str__(self):
        """String representation"""
        return self.__unicode__()

    def __unicode__(self):
        """Unicode representation"""
        return self.name

    class Meta:
        """Meta Class of Application class"""
        ordering = ('name',)
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')


class Session(models.Model):
    """Class for modeling sessions"""
    application = models.ForeignKey(Application, verbose_name=_('Application'), on_delete=models.PROTECT)
    uuid = models.UUIDField(verbose_name=_('Session UUID'))

    def __str__(self):
        """String representation"""
        return self.__unicode__()

    def __unicode__(self):
        """Unicode representation"""
        return f'{self.application.name}-{self.uuid}'

    class Meta:
        """Meta Class of Session class"""
        ordering = ('application__name', 'uuid')
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

    class Meta:
        """Meta Class of Event class"""
        verbose_name = _('Event Type')
        verbose_name_plural = _('Event Types')


class Event(models.Model):
    """Class for modeling events"""
    session = models.ForeignKey(Session, verbose_name=_('Session UUID'), on_delete=models.PROTECT)
    category = models.CharField(max_length=50, verbose_name=_('Category'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    data = models.JSONField(verbose_name=_('Payload of data'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Timestamp'))

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
