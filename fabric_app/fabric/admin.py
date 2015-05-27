from django.contrib import admin
from fabric.models import ShopProfile, DealerProfile


class ShopProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dealer', )


class DealerProfileAdmin(admin.ModelAdmin):
    list_display = ('dealer', 'url')

admin.site.register(ShopProfile, ShopProfileAdmin)
admin.site.register(DealerProfile, DealerProfileAdmin)
