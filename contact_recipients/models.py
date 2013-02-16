from django.db import models
from django.conf import settings

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Recipient(models.Model):
    """
    A model for determining which users will recieve contact messages from the
    contact form.
    """
    user = models.ForeignKey(USER_MODEL)

    def __unicode__(self):
        return u"{0}".format(self.user)

    class Meta:
        verbose_name = 'contact recipient'
        verbose_name_plural = 'contact recipients'
