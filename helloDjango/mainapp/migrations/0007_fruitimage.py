# Generated by Django 2.1.5 on 2019-08-27 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_storeentity_opened'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(max_length=50, upload_to='', verbose_name='图片存放路径')),
                ('width', models.IntegerField(verbose_name='图片的宽度')),
                ('height', models.IntegerField(verbose_name='图片的高度')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('fruit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.FruitEntity')),
            ],
            options={
                'verbose_name': '水果图片',
                'verbose_name_plural': '水果图片',
                'db_table': 't_fruitimage',
            },
        ),
    ]