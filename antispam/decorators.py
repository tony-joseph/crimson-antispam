from django.http import HttpResponseForbidden

from .models import SpamIP


def block_spam_ip(function):
    """Decorator to block access by ip addresses in spam ip list."""
    def wrap(request, *args, **kwargs):
        remote_ip = request.META['REMOTE_ADDR']
        if SpamIP.objects.filter(ip_address=remote_ip).exists():
            return HttpResponseForbidden()
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
