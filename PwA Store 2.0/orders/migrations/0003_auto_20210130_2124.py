# Generated by Django 3.1.5 on 2021-01-31 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210129_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shippingdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
