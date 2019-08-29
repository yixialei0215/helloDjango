from django.contrib import admin

# Register your models here.
from orderapp.models import OrderModel, AddressModel, OrderParticularsModel


class OrderAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'user_id', 'address_id')


class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'receive', 'receive_phone', 'receive_address')


class OrderParticularsAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_id', 'goods_id', 'cnt', 'get_price1', 'get_price', 'pay_type', 'pay_status')

    def get_price(self, obj):
        return obj.price

    def get_price1(self, obj):
        return obj.price1

    get_price.short_description = '总价'
    get_price1.short_description = '单价'


admin.site.register(OrderModel, OrderAdmin)
admin.site.register(AddressModel, AddressModelAdmin)
admin.site.register(OrderParticularsModel, OrderParticularsAdmin)
