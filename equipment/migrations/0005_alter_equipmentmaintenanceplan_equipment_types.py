# -*- coding: utf-8 -*-
# Generated by Django 4.1.2 on 2022-11-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0004_alter_equipment_is_active_equipmentmaintenanceplan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipmentmaintenanceplan",
            name="equipment_types",
            field=models.ManyToManyField(
                related_name="maintenance_plan",
                related_query_name="maintenance_plans",
                to="equipment.equipmenttype",
                verbose_name="Equipment Types",
            ),
        ),
    ]