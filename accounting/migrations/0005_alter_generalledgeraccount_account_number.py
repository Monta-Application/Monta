# Generated by Django 4.1.5 on 2023-01-11 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0004_alter_divisioncode_ap_account_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generalledgeraccount",
            name="account_number",
            field=models.CharField(
                help_text="The account number of the general ledger account.",
                max_length=20,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Account number must be in the format 0000-0000-0000-0000.",
                        regex="^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$",
                    )
                ],
                verbose_name="Account Number",
            ),
        ),
    ]