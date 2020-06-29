# Generated by Django 2.2.4 on 2020-06-26 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_payment_razor_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='productinfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productinfo', to='core.Order'),
        ),
    ]