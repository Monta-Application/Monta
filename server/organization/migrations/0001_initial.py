# Generated by Django 4.1.3 on 2022-12-04 00:03

import uuid

import django.db.models.deletion
import django_extensions.db.fields
import localflavor.us.models
import phonenumber_field.modelfields
from django.db import migrations, models

import organization.validators.organization


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Depot",
            fields=[
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
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the depot.",
                        max_length=255,
                        unique=True,
                        verbose_name="Depot Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="The description of the depot.",
                        max_length=255,
                        verbose_name="Depot Description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Depot",
                "verbose_name_plural": "Depots",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
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
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Organization Name"
                    ),
                ),
                (
                    "scac_code",
                    models.CharField(
                        help_text="The SCAC code for the organization.",
                        max_length=4,
                        verbose_name="SCAC Code",
                    ),
                ),
                (
                    "org_type",
                    models.CharField(
                        choices=[
                            ("Asset", "Asset"),
                            ("Brokerage", "Brokerage"),
                            ("Both", "Both"),
                        ],
                        default="Asset",
                        help_text="The type of organization.",
                        max_length=10,
                        verbose_name="Organization Type",
                    ),
                ),
                (
                    "timezone",
                    models.CharField(
                        default="America/New_York",
                        help_text="The timezone of the organization",
                        max_length=255,
                        validators=[
                            organization.validators.organization.validate_org_timezone
                        ],
                        verbose_name="Timezone",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("es", "Spanish")],
                        default="en",
                        help_text="The language of the organization",
                        max_length=2,
                        verbose_name="Language",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        default="USD",
                        help_text="The currency that the organization uses",
                        max_length=255,
                        verbose_name="Currency",
                    ),
                ),
                (
                    "date_format",
                    models.CharField(
                        default="MM/DD/YYYY",
                        help_text="Date Format",
                        max_length=255,
                        verbose_name="Date Format",
                    ),
                ),
                (
                    "time_format",
                    models.CharField(
                        default="HH:mm",
                        help_text="Time Format",
                        max_length=255,
                        verbose_name="Time Format",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="organizations/logo/",
                        verbose_name="Logo",
                    ),
                ),
                (
                    "authentication_bg",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="organizations/authentication_bg/",
                        verbose_name="Authentication Background",
                    ),
                ),
                (
                    "authentication_template",
                    models.CharField(
                        choices=[
                            ("default", "Default"),
                            ("corporate", "Corporate"),
                            ("creative", "Creative"),
                            ("fancy", "Fancy"),
                        ],
                        default="default",
                        help_text="The authentication template for the organization.",
                        max_length=10,
                        verbose_name="Authentication Template",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization",
                "verbose_name_plural": "Organizations",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="DepotDetail",
            fields=[
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
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "address_line_1",
                    models.CharField(
                        help_text="The address line 1 of the depot.",
                        max_length=255,
                        verbose_name="Address Line 1",
                    ),
                ),
                (
                    "address_line_2",
                    models.CharField(
                        blank=True,
                        help_text="The address line 2 of the depot.",
                        max_length=255,
                        verbose_name="Address Line 2",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        help_text="The city of the depot.",
                        max_length=255,
                        verbose_name="City",
                    ),
                ),
                (
                    "state",
                    localflavor.us.models.USStateField(
                        blank=True,
                        help_text="The state of the depot.",
                        max_length=2,
                        null=True,
                        verbose_name="State",
                    ),
                ),
                (
                    "zip_code",
                    localflavor.us.models.USZipCodeField(
                        blank=True,
                        help_text="The zip code of the depot.",
                        max_length=10,
                        null=True,
                        verbose_name="Zip Code",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        help_text="The phone number of the depot.",
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "alternate_phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        help_text="The alternate phone number of the depot.",
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Alternate Phone Number",
                    ),
                ),
                (
                    "fax_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        help_text="The fax number of the depot.",
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Fax Number",
                    ),
                ),
                (
                    "depot",
                    models.OneToOneField(
                        help_text="The depot that the depot detail belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="depot_details",
                        related_query_name="depot_detail",
                        to="organization.depot",
                        verbose_name="Depot",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        help_text="The organization that the depot detail belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="depot_details",
                        related_query_name="depot_detail",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Depot Detail",
                "verbose_name_plural": "Depot Details",
                "ordering": ["depot"],
            },
        ),
        migrations.AddField(
            model_name="depot",
            name="organization",
            field=models.ForeignKey(
                help_text="The organization that the depot belongs to.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="depots",
                related_query_name="depot",
                to="organization.organization",
                verbose_name="Organization",
            ),
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the department",
                        max_length=255,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="The description of the department",
                        verbose_name="Description",
                    ),
                ),
                (
                    "depot",
                    models.ForeignKey(
                        blank=True,
                        help_text="The depot that the department belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departments",
                        related_query_name="department",
                        to="organization.depot",
                        verbose_name="Depot",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        help_text="The organization that the department belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departments",
                        related_query_name="department",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
            },
        ),
    ]