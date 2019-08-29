from django.contrib import admin

from mainapp.models import UserEntity, CateTypeEntity, FruitEntity, StoreEntity, FruitImage, RealProfile, CartEntity, \
    FruitCartEntity


class UserAdmin(admin.ModelAdmin):
    # 表示列表中显示的字段
    list_display = ('id', 'name', 'phone')
    list_per_page = 1  # 每一页显示记录数
    list_filter = ('id', 'phone')  # 过滤器（一般配置类）
    search_fields = ('id', 'phone')  # 搜索字段


class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')


class FruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'source', 'price', 'category')


class FruitImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'width', 'height', 'fruit_id')


class StroeAdmin(admin.ModelAdmin):
    list_display = ('id_', 'name', 'city', 'address', 'store_type', 'logo', 'open_time')
    fields = ('name', 'city', 'address', 'store_type', 'logo', 'summary')


class RealProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'real_name', 'number', 'real_type')


class CartEntityAdmin(admin.ModelAdmin):
    list_display = ('user', 'no')


class FruitCartEntityAdmin(admin.ModelAdmin):
    # 显示字段可以引用关联
    list_display = ('cart', 'fruit', 'get_price1', 'cnt', 'get_price')

    def get_price1(self, obj):
        return obj.price1
    def get_price(self,obj):
        return obj.price
    get_price1.short_description = '小计'
    get_price.short_description = '总价'


# Register your models here.
# 将模型增加到站点中
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CateTypeEntity, CateTypeAdmin)
admin.site.register(FruitEntity, FruitAdmin)
admin.site.register(FruitImage, FruitImageAdmin)
admin.site.register(StoreEntity, StroeAdmin)
admin.site.register(RealProfile, RealProfileAdmin)
admin.site.register(CartEntity, CartEntityAdmin)
admin.site.register(FruitCartEntity, FruitCartEntityAdmin)
