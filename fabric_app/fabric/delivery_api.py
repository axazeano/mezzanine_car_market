import base64
import urllib
import urllib2
import json
from rest_framework.serializers import Serializer
from cartridge.shop.models import OrderItem
from fabric.models import ShopProfile
from fabric.serializers import DeliverySerializer
from rest_framework.authentication import Token

__author__ = 'vladimir'


class Connection(object):
    def __init__(self, user, token, url):
        self.user = user
        self.token = token
        self.url = url
        self.credentials = base64.encodestring('%s:%s' % (self.user, self.token)).replace('\n', '')

    def get(self, additional_path, data):
        request = urllib2.Request(self.url + additional_path)
        request.add_header("Authorization", "token %s" % self.credentials)
        return urllib2.urlopen(request).read()

    def post(self, additional_path, post_data):
        data = urllib.urlencode(post_data)
        request = urllib2.Request(self.url + additional_path, data)
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.URLError:
            response = None

        return response

    def heartbeat(self, heartbeat_path):
        pass


class DeliveryFramework:
    CREATE_DELIVERY_PATH = '/api/delivery/create/'

    def __init__(self):
        pass

    def create_delivery(self, dealer, token, delivery_object):
        connection = Connection(dealer, token, dealer.url)
        connection.post(delivery_object, self.CREATE_DELIVERY_PATH)

    def order_delivery_handler(self, request, order_form, order):
        delivery = create_delivery_json_object(order, request.user)
        dealer = ShopProfile(user=request.user).dealer
        token = Token(user=ShopProfile(user=request.user).dealer)

        self.create_delivery_json_object(dealer, token, delivery)


def create_delivery_json_object(order, user):
    order_item = OrderItem.objects.get(order_id=order.pk)
    delivery = {'description': order_item.description,
               'quantity': str(order_item.quantity),
               'cost': str(order_item.total_price),
               'shop_name':ShopProfile.objects.get(user=user).name}
    return json.dumps(delivery)

class Delivery(object):
    def __init__(self, product_description, quantity, cost, shop_name):
        self.product_description = product_description
        self.quantity = quantity
        self.cost = cost
        self.shop_name = shop_name


def to_json(something):
        return json.dumps(something)


