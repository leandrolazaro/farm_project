# Generated by Django 2.2 on 2022-08-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_base', '0003_auto_20220828_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='municipality',
            field=models.CharField(max_length=255, null=True, verbose_name='Municipality'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='state',
            field=models.CharField(max_length=255, null=True, verbose_name='State'),
        ),
    ]