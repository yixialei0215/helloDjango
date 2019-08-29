# Generated by Django 2.1.5 on 2019-08-29 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_fruitentity_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='标签名')),
                ('order_num', models.IntegerField(default=1, verbose_name='序号')),
            ],
            options={
                'verbose_name': '标签信息',
                'verbose_name_plural': '标签信息',
                'db_table': 't_tag',
                'ordering': ['-order_num'],
            },
        ),
        migrations.AlterField(
            model_name='fruitentity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='mainapp.CateTypeEntity'),
        ),
        migrations.AddField(
            model_name='fruitentity',
            name='tags',
            field=models.ManyToManyField(db_table='t_fruit_tags', related_name='fruits', to='mainapp.TagEntity', verbose_name='所有标签'),
        ),
    ]
