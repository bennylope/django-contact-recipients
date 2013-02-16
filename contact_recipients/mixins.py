from django.conf import settings

from .models import Recipient


class RecipientsMixin(object):
    """
    A mixin for sending the results to a list of recipients.
    """
    def get_recipients(self):
        emails = [recipient.user.email for recipient in
                Recipient.objects.all().select_related('user') if
                recipient.user.email]
        return emails if emails else [mail_tuple[1] for
                mail_tuple in settings.MANAGERS]
    recipient_list = get_recipients
