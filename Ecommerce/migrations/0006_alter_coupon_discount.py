# Generated by Django 3.2.16 on 2022-11-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0005_auto_20221128_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.FloatField(),
        ),
    ]
