from django.test import TestCase
from django.db.models import get_model
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

from django_dynamic_fixture import G
from override_settings import override_settings

from .models import Recipient
from .mixins import RecipientsMixin


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


def get_user_model():
    """Fill-in for functionality not available in Django < 1.5"""
    try:
        klass = get_model(USER_MODEL.split('.')[0], USER_MODEL.split('.')[1])
    except:
        raise ImproperlyConfigured("Your user class, {0}, is improperly defined".format(USER_MODEL))
    return klass


class RecipientMixinTests(TestCase):

    def test_settings_recipients(self):
        """
        Ensure that the contact list consists of site manager email addresses
        """
        Recipient.objects.all().delete()
        managers = (('Bubba', 'bubba@gump.com'),)
        mix = RecipientsMixin()
        with override_settings(MANAGERS=managers):
            self.assertEqual(mix.recipient_list(), ['bubba@gump.com'])

    def test_database_recipients(self):
        """
        Ensure that the contact list consists of specified user email addresses
        """
        user1 = G(get_user_model(), is_staff=True)
        user2 = G(get_user_model(), is_staff=True)
        recipient1 = G(Recipient, user=user1)
        recipient2 = G(Recipient, user=user2)

        mix = RecipientsMixin()
        self.assertEqual(mix.recipient_list(),
                [user1.email, user2.email])
