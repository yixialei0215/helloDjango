# Generated by Django 2.1.5 on 2019-08-28 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_fruitcartentity'),
        ('orderapp', '0002_auto_20190828_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressmodel',
            name='u_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserEntity', verbose_name='用户id'),
            preserve_default=False,
        ),
    ]