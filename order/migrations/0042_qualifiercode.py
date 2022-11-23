# Generated by Django 4.1.3 on 2022-11-23 18:31

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0007_alter_depot_description_alter_depot_name_and_more"),
        ("order", "0041_movement_stop_serviceincident_reasoncode"),
    ]

    operations = [
        migrations.CreateModel(
            name="QualifierCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Code of the Qualifier Code",
                        max_length=255,
                        unique=True,
                        verbose_name="Code",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Description of the Qualifier Code",
                        max_length=100,
                        verbose_name="Description",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        help_text="Organization",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)ss",
                        related_query_name="%(class)s",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Qualifier Code",
                "verbose_name_plural": "Qualifier Codes",
                "ordering": ["code"],
            },
        ),
    ]