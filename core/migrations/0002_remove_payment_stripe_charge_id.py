# Generated by Django 2.2.4 on 2020-06-26 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='stripe_charge_id',
        ),
    ]
