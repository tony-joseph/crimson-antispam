from django.db import IntegrityError

from .models import SpamIP


def add_spam_ip(ip_address):
    """ Function to add a new ip address to spam list.
    :param spam_ip: either IPv4 or IPv6 address.
    :return: None
    """

    try:
        SpamIP.objects.create(ip_address=ip_address)
    except IntegrityError:
        # If ip address is already in database, ignore
        pass


def bulk_add_spam_ip(ip_address_list):
    """ Function to add a list or tuple of ip addresses into spam list.
    :param ip_address_list: list or tuple of IPv4 or IPv6 addresses.
    :return: None
    """

    for ip_address in ip_address_list:
        add_spam_ip(ip_address)


def is_spam_ip(ip_address):
    """ Checks whether the ip address is in spam list.
    :param ip_address: IPv4 or IPv6 ip address
    :return: True if the ip address is in spam list, else False
    """

    return SpamIP.objects.filter(ip_address=ip_address).exists()


def remove_spam_ip(ip_address):
    """ Removes the ip address from spam list if it is in spam list.
    :param ip_address: IPv4 or IPv6 ip address
    :return: None
    """

    SpamIP.objects.filter(ip_address=ip_address).delete()
