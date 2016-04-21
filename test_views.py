from django.http import HttpResponse

from antispam.decorators import block_spam_ip, throttle_requests


def index(request):
    return HttpResponse('Test view')


@block_spam_ip
def blocked_by_decorator(request):
    return HttpResponse('Blocked by decorator from spam ip.')


@throttle_requests
def throttled_by_decorator(request):
    return HttpResponse('Throttled by decorator.')
