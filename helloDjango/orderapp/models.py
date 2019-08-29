from django.db import models
from django.db.models import Q

from mainapp.models import FruitEntity, UserEntity


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间',
                                       auto_now_add=True)
    last_time = models.DateTimeField(verbose_name='更新时间',
                                     auto_now=True)

    class Meta:
        abstract = True  # 抽象的模型类，即不会创建表


# 声明QuerySet 或Manager的子类
class OrderManager(models.Manager):
    # 获取查询结果集对象QuerySet
    def get_queryset(self):
        return super().get_queryset().filter(~Q(pay_status=5))


# Create your models here.

class AddressModel(models.Model):
    class Meta:
        db_table = 't_adress'
        verbose_name = verbose_name_plural = '收货详情'

    u_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE,
                             verbose_name='用户id')
    receive = models.CharField(max_length=20,
                               verbose_name='收货人')
    receive_phone = models.CharField(max_length=11,
                                     verbose_name='收货人电话')
    receive_address = models.TextField(verbose_name='收获地址')

    def __str__(self):
        return self.receive_address


# 订单表
class OrderModel(models.Model):
    num = models.CharField(max_length=20,
                           primary_key=True,
                           verbose_name='订单号')
    title = models.CharField(max_length=100,
                             verbose_name='订单名称')
    user_id = models.ForeignKey(UserEntity,
                                on_delete=models.CASCADE,
                                verbose_name='用户id')
    address_id = models.ForeignKey(AddressModel, on_delete=models.CASCADE,
                                   verbose_name='收货地址')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_order'
        verbose_name = verbose_name_plural = '订单表'


# 订单详情表
class OrderParticularsModel(BaseModel):
    class Meta:
        db_table = 't_orderparticulars'
        verbose_name = verbose_name_plural = '订单详情表'

    num_id = models.ForeignKey(OrderModel,
                               on_delete=models.CASCADE,
                               verbose_name='订单名称')
    goods_id = models.ForeignKey(FruitEntity,
                                 on_delete=models.CASCADE,
                                 verbose_name='商品id')
    cnt = models.IntegerField(verbose_name='商品数量',
                              default=1)
    pay_type = models.IntegerField(choices=((0, '余额支付'),
                                            (1, '银联支付'),
                                            (2, '支付宝'),
                                            (3, '微信支付')),
                                   verbose_name='支付方式',
                                   default=0)
    pay_status = models.IntegerField(choices=((0, '待支付'),
                                              (1, '已支付'),
                                              (2, '待收货'),
                                              (3, '已收货'),
                                              (4, '完成'),
                                              (5, '已取消')),
                                     verbose_name='订单状态',
                                     default=0)

    objects = OrderManager()  # 显性创建 objects

    @property
    def price(self):
        return round(self.cnt * self.goods_id.price, 2)

    @property
    def price1(self):
        return round(self.goods_id.price, 2)

    def __str__(self):
        return self.num_id.title
