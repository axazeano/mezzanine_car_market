from django.contrib.auth.models import User
from django.db import models


class ShopProfile(models.Model):
    user = models.ForeignKey(User, related_name='shop_user')
    dealer = models.ForeignKey(User, related_name='dealer_user')
    name = models.CharField(max_length=200)


class DealerProfile(models.Model):
    dealer = models.ForeignKey(User)
    url = models.CharField(max_length=200)
    token = models.CharField(max_length=200)



