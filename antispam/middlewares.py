from django.http import HttpResponseForbidden

from .models import SpamIP


class BlockSpamIPMiddleware(object):
    """Middleware to block access to ip addresses in spam list."""

    def process_request(self, request):
        remote_ip = request.META['REMOTE_ADDR']
        if SpamIP.objects.filter(ip_address=remote_ip).exists():
            return HttpResponseForbidden()
