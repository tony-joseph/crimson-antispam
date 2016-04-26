from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone

from .models import SpamIP, IPAcessLog


def block_spam_ip(function):
    """Decorator to block access by ip addresses in spam ip list."""

    def wrap(request, *args, **kwargs):
        remote_ip = request.META['REMOTE_ADDR']
        if SpamIP.objects.filter(ip_address=remote_ip).exists():
            return HttpResponse('Access denied: Your IP address is in spam list.', status=403)
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def throttle_requests(function):
    """Decorator to block request if interval between requests is less than allowed interval."""

    def wrap(request, *args, **kwargs):
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
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
