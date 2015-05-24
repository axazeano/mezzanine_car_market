from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from mezzanine.core.models import Displayable
from hashlib import sha256
from django.utils.translation import (ugettext, ugettext_lazy as _)
from cartridge.shop.models import Product

__author__ = 'vladimir'

class ShippingProvider(Displayable, models.Model):
    """
    Credential of provider
    Dealer registering in system as user
    provider: user of dealer
    name: name of dealer
    token_paraphrase: string for generate token. After create token will set blank and string send to dealer
    token: auth token. Read-only field in admin, can be changed by set new token_paraphrase
    token_last_update: time and date of last change token. Read-only field, updates when user changed token
    token_change_reason: reason of changed token
    token_change_by: user, who changed token. Read-only field, updates when user changed token
    """
    provider = models.ForeignKey(User, related_name='provider')
    name = models.CharField(max_length=200)
    token_paraphrase = models.CharField(max_length=200, blank=True, null=True, default='')
    token = models.CharField(max_length=200, blank=True, null=True, default='')
    token_last_update_date = models.DateTimeField(default=now)
    token_change_reason = models.CharField(max_length=250, default='')
    token_change_by = models.ForeignKey(User, related_name='token_change_by')

    class Meta:
        verbose_name = _("Shipping provider")
        verbose_name_plural = _("Shipping providers")

    def save(self, *args, **kwargs):
        self.token = sha256(self.token_paraphrase).hexdigest()
        self.token_last_update_date = now()
        self.token_paraphrase = ''
        super(ShippingProvider, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("shipping_provider", (), {"slug": self.slug})



