# Generated by Django 4.2.11 on 2024-04-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0003_alter_passwordentry_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordentry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]