from django.http import HttpResponseForbidden
from django.conf import settings
from django.utils import timezone

from .models import SpamIP, IPAcessLog


class BlockSpamIPMiddleware(object):
    """Middleware to block access to ip addresses in spam list."""

    def process_request(self, request):
        remote_ip = request.META['REMOTE_ADDR']
        if SpamIP.objects.filter(ip_address=remote_ip).exists():
            return HttpResponseForbidden()


class ThrottleRequestsMiddleware(object):
    """Middleware to block simultaneous requests from same ip."""

    def process_request(self, request):
        allowed_interval = settings.ANTISPAM_SETTINGS.get('REQUEST_INTERVAL', 1)
        remote_ip = request.META['REMOTE_ADDR']

        try:
            access_log = IPAcessLog.objects.get(ip_address=remote_ip)
            interval = timezone.now() - access_log.last_accessed

            # Update access log with current access time.
            access_log.last_accessed = timezone.now()
            access_log.save()

            if interval.seconds < allowed_interval:
                return HttpResponseForbidden()
        except IPAcessLog.DoesNotExist:
            IPAcessLog.objects.create(ip_address=remote_ip, last_accessed=timezone.now())
