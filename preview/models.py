import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class BetaSignup(models.Model):
    """
    Model to store our pre-beta signups
    """ 
    first_name = models.CharField(_('First Name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=75, blank=True)
    email = models.EmailField(_('Email Address'), unique=True)
    key = models.CharField(_('unsubscription key'), max_length=40)

    contacted = models.BooleanField(_('Contacted'), default=False)
    registered = models.BooleanField(_('Registered'), default=False)

    created = models.DateTimeField(_('Created'), default=datetime.datetime.now)

    class Meta:
        verbose_name = _('Preview Signup')
        verbose_name_plural = _('Preview Signups')

    def __unicode__(self):
        return 'Preview Signup - %s' % self.email

