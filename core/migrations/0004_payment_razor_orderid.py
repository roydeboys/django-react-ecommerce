# Generated by Django 2.2.4 on 2020-06-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_payment_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='razor_orderid',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
    ]
