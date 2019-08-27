from django.contrib import admin

from mainapp.models import UserEntity, CateTypeEntity, FruitEntity, StoreEntity


class UserAdmin(admin.ModelAdmin):
    # 表示列表中显示的字段
    list_display = ('id', 'name', 'phone')
    list_per_page = 1  # 每一页显示记录数
    list_filter = ('id', 'phone')  # 过滤器（一般配置类）
    search_fields = ('id', 'phone')  # 搜索字段


class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')


class FruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'price', 'category')


# class FruitImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'url', 'width', 'height', 'fruit_id')


class StroeAdmin(admin.ModelAdmin):
    list_display = ('id_', 'name', 'city', 'address', 'store_type', 'logo','open_time')
    fields = ('name', 'city', 'address', 'store_type', 'logo', 'summary')


# Register your models here.
# 将模型增加到站点中
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CateTypeEntity, CateTypeAdmin)
admin.site.register(FruitEntity, FruitAdmin)
# admin.site.register(FruitImage, FruitImageAdmin)
admin.site.register(StoreEntity, StroeAdmin)
