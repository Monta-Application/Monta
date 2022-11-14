# Generated by Django 4.1.2 on 2022-11-07 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0006_alter_depotdetail_address_line_1_and_more"),
        ("accounts", "0011_alter_userprofile_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                related_query_name="user",
                to="organization.organization",
                verbose_name="Organization",
            ),
            preserve_default=False,
        ),
    ]