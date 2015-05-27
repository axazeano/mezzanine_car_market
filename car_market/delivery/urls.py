from car_market.delivery.views import DeliveryViewSet

__author__ = 'vladimir'

from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'main', DeliveryViewSet)


urlpatterns = patterns(
    'delivery.views',
    url(r'^delivery/add/$', 'create_new_delivery', name='create_new_delivery'),
    url(r'^delivery/', include(router.urls))
)
