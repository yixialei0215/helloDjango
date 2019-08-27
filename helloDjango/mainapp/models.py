import uuid

from django.db import models


# Create your models here.
# 客户的用户表


class UserEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='账号')
    age = models.IntegerField(default=0, verbose_name='年龄')
    phone = models.CharField(max_length=11,
                             verbose_name='手机号',
                             blank=True,  # 站点的表单字段值可以为空
                             null=True  # 数据表的字段可以是null
                             )

    def __str__(self):
        return self.name

    class Meta:
        # 设定表名
        db_table = 'app_user'
        verbose_name = '客户管理'
        # 设置复数的表示方式
        verbose_name_plural = verbose_name


# 水果分类模型
class CateTypeEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')
    order_num = models.IntegerField(verbose_name='排序')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'mainapp'  # 指定应用的名称
        db_table = 't_catetype'
        ordering = ['order_num']  # 指定排序字段。 - 表示降序，默认升序
        verbose_name = '水果分类'
        verbose_name_plural = verbose_name


class FruitEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='水果名')
    price = models.FloatField(verbose_name='价格', )
    source = models.CharField(max_length=30, verbose_name='原产地')

    category = models.ForeignKey(CateTypeEntity,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '-' + self.source

    class Meta:
        db_table = 't_fruit'
        verbose_name = '水果'
        verbose_name_plural = verbose_name


'''
class FruitImage(models.Model):
    fruit_id = models.ForeignKey(FruitEntity, on_delete=models.CASCADE)
    url = models.ImageField(max_length=50, verbose_name='图片存放路径')
    width = models.IntegerField(verbose_name='图片的宽度')
    height = models.IntegerField(verbose_name='图片的高度')
    name = models.CharField(max_length=20, verbose_name='名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_fruitimage'
        verbose_name = '水果图片'
        verbose_name_plural = verbose_name
'''


class StoreEntity(models.Model):
    # 默认情况下，模型会自动创建主键id字段——隐式
    # 但是，也可以以显示的方式声明主键（primary key）
    id = models.UUIDField(primary_key=True,
                          verbose_name='店号')
    name = models.CharField(max_length=20, verbose_name='商店名', unique=True)
    # 表中对应的字段是type_
    store_type = models.IntegerField(choices=((0, '自营'), (1, '第三方')),
                                     verbose_name='商店类型',
                                     db_column='tyep_')
    phone = models.CharField(max_length=11,
                             verbose_name='老板电话')
    address = models.CharField(max_length=50,
                               verbose_name='商店地址')
    #  支持城市搜索，所以创建city索引
    city = models.CharField(max_length=20,
                            verbose_name='商品所在城市',
                            db_index=True)
    logo = models.ImageField(verbose_name='LOGO',
                             upload_to='store',
                             width_field='logo_width',
                             height_field='logo_height',
                             null=True,
                             blank=True)

    logo_width = models.IntegerField(verbose_name='LOGO width',
                                     null=True)
    logo_height = models.IntegerField(verbose_name='LOGO height',
                                      null=True)

    summary = models.TextField(verbose_name='介绍', blank=True,
                               null=True)
    opened = models.BooleanField(verbose_name='是否开业',
                                 default=False)

    create_time = models.DateField(verbose_name='成立时间',
                                   auto_now_add=True)
    last_time = models.DateField(verbose_name='最后变更时间',
                                 auto_now=True)

    @property
    def open_time(self):
        print(self.create_time)
        return self.create_time

    # 站点显示对象的字符串信息
    def __str__(self):
        return self.name + "-" + self.city

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # 调用模型保存方法时被调用
        if not self.id:  # 判断是否为新增
            self.id = uuid.uuid4().hex
        super().save()

    def id_(self):
        # return str(self.id).replace('-', '')
        return self.id.hex

    class Meta:  # 元数据
        db_table = 't_store'
        unique_together = (('name', 'city'),)
        verbose_name = '商店信息'
        verbose_name_plural = verbose_name
