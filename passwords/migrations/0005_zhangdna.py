# Generated by Django 4.2.11 on 2024-04-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0004_alter_passwordentry_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZhangDna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shouzhi', models.CharField(max_length=100)),
                ('Leixing', models.CharField(max_length=100)),
                ('Jiage', models.CharField(max_length=100)),
            ],
        ),
    ]
