# Generated by Django 4.1.3 on 2022-12-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="code",
            field=models.CharField(
                default=1, max_length=100, unique=True, verbose_name="Code"
            ),
            preserve_default=False,
        ),
    ]
