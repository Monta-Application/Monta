# Generated by Django 4.1.3 on 2022-11-26 05:19

from django.db import migrations
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0058_order_order_origin_destination_check"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="order",
            name="order_origin_destination_check",
        ),
    ]
