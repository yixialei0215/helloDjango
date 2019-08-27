# Generated by Django 2.1.5 on 2019-08-27 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CateTypeEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名')),
                ('order_num', models.IntegerField(verbose_name='排序')),
            ],
            options={
                'verbose_name': '水果分类',
                'verbose_name_plural': '水果分类',
                'db_table': 't_catetype',
                'ordering': ['order_num'],
            },
        ),
        migrations.CreateModel(
            name='FruitEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='水果名')),
                ('price', models.FloatField(verbose_name='价格')),
                ('source', models.CharField(max_length=30, verbose_name='原产地')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.CateTypeEntity')),
            ],
            options={
                'verbose_name': '水果',
                'verbose_name_plural': '水果',
                'db_table': 't_fruit',
            },
        ),
        migrations.CreateModel(
            name='StoreEntity',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='店号')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='商店名')),
                ('store_type', models.IntegerField(choices=[(0, '自营'), (1, '第三方')], db_column='tyep_', verbose_name='商店类型')),
                ('phone', models.CharField(max_length=11, verbose_name='老板电话')),
                ('address', models.CharField(max_length=50, verbose_name='商店地址')),
                ('city', models.CharField(db_index=True, max_length=20, verbose_name='商品所在城市')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='成立时间')),
                ('last_time', models.DateField(auto_now=True, verbose_name='最后变更时间')),
            ],
            options={
                'verbose_name': '商店信息',
                'verbose_name_plural': '商店信息',
                'db_table': 't_store',
            },
        ),
        migrations.CreateModel(
            name='UserEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='账号')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '客户管理',
                'verbose_name_plural': '客户管理',
                'db_table': 'app_user',
            },
        ),
        migrations.AlterUniqueTogether(
            name='storeentity',
            unique_together={('name', 'city')},
        ),
    ]
