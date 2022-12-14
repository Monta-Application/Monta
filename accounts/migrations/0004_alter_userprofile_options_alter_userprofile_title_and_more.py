# Generated by Django 4.1.3 on 2022-12-05 04:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_token_expires"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "ordering": ["-created"],
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
            },
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userprofile",
                related_query_name="userprofiles",
                to="accounts.jobtitle",
                verbose_name="Job Title",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userprofile",
                related_query_name="userprofiles",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
