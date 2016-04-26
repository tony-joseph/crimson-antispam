from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone

from .models import SpamIP, IPAcessLog


class BlockSpamIPMiddleware(object):
    """Middleware to block access to ip addresses in spam list."""

    def process_request(self, request):
        remote_ip = request.META['REMOTE_ADDR']
        if SpamIP.objects.filter(ip_address=remote_ip).exists():
            return HttpResponse('Access denied: Your IP address is in spam list.', status=403)


class ThrottleRequestsMiddleware(object):
    """Middleware to block simultaneous requests from same ip."""

    def process_request(self, request):
        allowed_interval = settings.ANTISPAM_SETTINGS.get('REQUEST_INTERVAL', 1000)
        remote_ip = request.META['REMOTE_ADDR']

        try:
            access_log = IPAcessLog.objects.get(ip_address=remote_ip)
            interval = timezone.now() - access_log.last_accessed

            # Update access log with current access time.
            access_log.last_accessed = timezone.now()
            access_log.save()

            # Calculate interval in milliseconds
            interval_in_ms = (interval.seconds * 1000) + (interval.microseconds // 1000)

            # Raise 403 if interval is less than allowed interval
            if interval_in_ms < allowed_interval:
                return HttpResponse('Access denied: Too many requests from your IP address.', status=429)

        except IPAcessLog.DoesNotExist:
            IPAcessLog.objects.create(ip_address=remote_ip, last_accessed=timezone.now())
