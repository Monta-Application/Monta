# Generated by Django 4.1.3 on 2022-11-15 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0007_equipment_primary_worker_equipment_secondary_worker"),
        ("order", "0018_orderdocumentation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movement",
            name="equipment",
            field=models.ForeignKey(
                blank=True,
                help_text="Equipment of the Movement",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="movements",
                related_query_name="movement",
                to="equipment.equipment",
                verbose_name="Equipment",
            ),
        ),
    ]
