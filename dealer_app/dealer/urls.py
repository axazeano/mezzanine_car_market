__author__ = 'vladimir'

from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    'dealer.views',
    url(r'^test/$', 'test_connection', name='create_new_delivery'),
    url(r'delivery/create', 'create_delivery', name='create_delivery')
)
