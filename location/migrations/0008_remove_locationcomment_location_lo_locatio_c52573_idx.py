# Generated by Django 4.1.3 on 2022-11-21 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0007_rename_category_location_location_category"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="locationcomment",
            name="location_lo_locatio_c52573_idx",
        ),
    ]
