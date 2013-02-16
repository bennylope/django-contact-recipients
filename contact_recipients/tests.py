from django.contrib.auth import get_user_model
from django.test import TestCase

from django_dynamic_fixture import G
from override_settings import override_settings

from .models import Recipient
from .mixins import RecipientsMixin


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
