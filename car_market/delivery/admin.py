from django.contrib import admin
from car_market.delivery.models import ShippingProvider, Delivery, DeliveryAudit

__author__ = 'vladimir'


class ShippingProviderAdmin(admin.ModelAdmin):
    list_display = ("provider", "name", "token_paraphrase", "token", "token_last_update_date",
                    "token_change_reason", "token_change_by",)
    # list_editable = ("provider", "name", "token_paraphrase", "token_change_reason",)
    readonly_fields = ('token', 'token_last_update_date', 'token_change_by')

    def save_model(self, request, obj, form, change):
        obj.token_change_by = request.user
        obj.save()


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('provider', 'dealer_delivery_id', 'delivery_status', 'product', 'product_count', 'cost', 'date')
    # list_editable = ("provider", "name", "token_paraphrase", "token_change_reason",)
    #readonly_fields = ('token', 'token_last_update_date', 'token_change_by')


admin.site.register(ShippingProvider, ShippingProviderAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryAudit)