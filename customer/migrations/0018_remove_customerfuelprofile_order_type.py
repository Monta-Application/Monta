# Generated by Django 4.1.3 on 2022-11-23 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0017_alter_customerfuelprofile_days_to_use_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customerfuelprofile",
            name="order_type",
        ),
    ]