# Generated by Django 4.1.3 on 2022-11-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0012_remove_order_destination_appoint_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="bol_number",
            field=models.CharField(
                help_text="BOL Number", max_length=255, verbose_name="BOL Number"
            ),
        ),
    ]