# Generated by Django 4.1.4 on 2022-12-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipmenttype",
            name="id",
            field=models.CharField(
                help_text="ID of the equipment manufacturer.",
                max_length=50,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.DeleteModel(
            name="EquipmentTypeDetail",
        ),
    ]
