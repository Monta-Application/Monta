# Generated by Django 4.1.3 on 2022-11-14 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0013_alter_order_bol_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="destination_appointment",
        ),
        migrations.RemoveField(
            model_name="order",
            name="origin_appointment",
        ),
        migrations.AlterField(
            model_name="order",
            name="commodity",
            field=models.ForeignKey(
                help_text="Commodity",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orders",
                related_query_name="order",
                to="order.commodity",
                verbose_name="Commodity",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("N", "New"),
                    ("P", "In Progress"),
                    ("C", "Completed"),
                    ("B", "Billed"),
                    ("V", "Voided"),
                ],
                default="N",
                max_length=20,
                verbose_name="Status",
            ),
        ),
    ]