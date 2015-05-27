from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from mezzanine.core.models import Displayable
from hashlib import sha256
from django.utils.translation import (ugettext, ugettext_lazy as _)
from cartridge.shop.models import Product

__author__ = 'vladimir'

class ShippingProvider(models.Model):
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
    provider_url = models.CharField(max_length=200)
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


class DeliveryStatus(models.Model):
    status = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.status


class Delivery(models.Model):
    """
    Deliveries model.
    provider : dealer, which delivered products to shop
    delivery_dealer_id : delivery has uid on dealer's side
    delivery_status : status of delivery
    product : which product should be delivered to shop
    product_count : how many product should be in delivery
    delivery_cost : cost of delivery
    """
    provider = models.ForeignKey(User)
    dealer_delivery_id = models.IntegerField(_("UID on dealer side"))
    delivery_status = models.ForeignKey(DeliveryStatus)
    product = models.ForeignKey(Product)
    product_count = models.FloatField()
    cost = models.FloatField()
    date = models.DateField(default=now)

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')


class DeliveryAction(models.Model):
    action = models.CharField(max_length=120)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = _("Delivery action")
        verbose_name_plural = _("Delivery actions")


class DeliveryAudit(models.Model):
    delivery = models.ForeignKey(Delivery)
    delivery_action = models.ForeignKey(DeliveryAction)
    action_date = models.DateTimeField(default=now)
    action_create_by = models.ForeignKey(User)
    action_description = models.CharField(max_length=300)

    class Meta:
        verbose_name = _("Delivery audit")
        verbose_name_plural = _("Delivery audits")


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField()
    bio = models.TextField()
