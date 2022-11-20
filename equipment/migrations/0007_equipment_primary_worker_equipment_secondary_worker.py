# Generated by Django 4.1.3 on 2022-11-15 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("worker", "0021_alter_worker_address_line_2_alter_worker_code_and_more"),
        ("equipment", "0006_alter_equipment_model_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="equipment",
            name="primary_worker",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_equipment",
                related_query_name="primary_equipment",
                to="worker.worker",
                verbose_name="Primary Worker",
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="secondary_worker",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="secondary_equipment",
                related_query_name="secondary_equipment",
                to="worker.worker",
                verbose_name="Secondary Worker",
            ),
        ),
    ]