from django.db import models


class SpamIP(models.Model):
    """Model to store spam ip addresses."""
    ip_address = models.GenericIPAddressField(unique=True, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address


class IPAcessLog(models.Model):
    ip_address = models.GenericIPAddressField(unique=True, db_index=True)
    last_accessed = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address
