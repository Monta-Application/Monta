# -*- coding: utf-8 -*-
# Generated by Django 4.1.2 on 2022-11-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0005_depot_depotdetail_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="depotdetail",
            name="address_line_1",
            field=models.CharField(
                help_text="The address line 1 of the depot.",
                max_length=255,
                verbose_name="Address Line 1",
            ),
        ),
        migrations.AlterField(
            model_name="depotdetail",
            name="address_line_2",
            field=models.CharField(
                blank=True,
                help_text="The address line 2 of the depot.",
                max_length=255,
                null=True,
                verbose_name="Address Line 2",
            ),
        ),
    ]
