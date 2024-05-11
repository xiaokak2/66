# Generated by Django 4.2.11 on 2024-05-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='收货人姓名')),
                ('phone', models.CharField(max_length=15, verbose_name='手机号码')),
                ('area', models.CharField(max_length=255, verbose_name='所在地区')),
                ('address', models.TextField(verbose_name='详细地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认地址')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]