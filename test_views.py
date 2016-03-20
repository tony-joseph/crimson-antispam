from django.http import HttpResponse

from antispam.decorators import block_spam_ip


def index(request):
    return HttpResponse('Test view')


@block_spam_ip
def blocked_by_decorator(request):
    return HttpResponse('Blocked by decorator from spam ip.')
