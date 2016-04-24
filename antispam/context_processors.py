from .models import SpamIP


def antispam_processor(request):
    """Context processor to make SITE_CONFIG available to all templates."""

    return {'is_spam_ip': SpamIP.objects.filter(ip_address=request.META['REMOTE_ADDR']).exists()}
