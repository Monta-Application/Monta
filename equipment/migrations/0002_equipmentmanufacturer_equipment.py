# -*- coding: utf-8 -*-
# Generated by Django 4.1.2 on 2022-10-31 02:31

import django.db.models.deletion
import django_extensions.db.fields
import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0004_alter_organization_language_and_more"),
        ("equipment", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EquipmentManufacturer",
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
                    models.CharField(
                        help_text="ID of the equipment manufacturer.",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of the equipment manufacturer.",
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
                "verbose_name": "Equipment Manufacturer",
                "verbose_name_plural": "Equipment Manufacturers",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Equipment",
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
                    models.CharField(
                        help_text="ID of the equipment.",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Whether the equipment type detail is active.",
                        verbose_name="Active",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of the equipment.",
                        verbose_name="Description",
                    ),
                ),
                (
                    "license_plate_number",
                    models.CharField(
                        blank=True,
                        help_text="License plate number of the equipment.",
                        max_length=50,
                        verbose_name="License Plate Number",
                    ),
                ),
                (
                    "vin_number",
                    models.CharField(
                        blank=True,
                        help_text="VIN number of the equipment.",
                        max_length=17,
                        null=True,
                        verbose_name="VIN Number",
                    ),
                ),
                (
                    "odometer",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Odometer of the equipment.",
                        verbose_name="Odometer",
                    ),
                ),
                (
                    "engine_hours",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Engine hours of the equipment.",
                        verbose_name="Engine Hours",
                    ),
                ),
                (
                    "manufactured_date",
                    models.DateField(
                        blank=True,
                        help_text="Manufactured date of the equipment.",
                        null=True,
                        verbose_name="Manufactured Date",
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        blank=True,
                        help_text="Model of the equipment.",
                        max_length=50,
                        null=True,
                        verbose_name="Model",
                    ),
                ),
                (
                    "model_year",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Model year of the equipment.",
                        null=True,
                        verbose_name="Model Year",
                    ),
                ),
                (
                    "state",
                    localflavor.us.models.USStateField(
                        blank=True,
                        help_text="State of the equipment.",
                        max_length=2,
                        null=True,
                        verbose_name="State",
                    ),
                ),
                (
                    "leased",
                    models.BooleanField(
                        default=False,
                        help_text="Leased of the equipment.",
                        verbose_name="Leased",
                    ),
                ),
                (
                    "leased_date",
                    models.DateField(
                        blank=True,
                        help_text="Leased date of the equipment.",
                        null=True,
                        verbose_name="Leased Date",
                    ),
                ),
                (
                    "hos_exempt",
                    models.BooleanField(
                        default=False,
                        help_text="HOS exempt of the equipment.",
                        verbose_name="HOS Exempt",
                    ),
                ),
                (
                    "aux_power_unit_type",
                    models.CharField(
                        choices=[
                            ("none", "None"),
                            ("apu", "APU"),
                            ("bunk-heater", "Bunk Heater"),
                            ("hybrid", "Hybrid"),
                        ],
                        default="none",
                        help_text="Auxiliary power unit type of the equipment.",
                        max_length=50,
                        verbose_name="Auxiliary Power Unit Type",
                    ),
                ),
                (
                    "fuel_draw_capacity",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Fuel draw capacity of the equipment.",
                        verbose_name="Fuel Draw Capacity",
                    ),
                ),
                (
                    "num_of_axles",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Number of axles of the equipment.",
                        verbose_name="Number of Axles",
                    ),
                ),
                (
                    "transmission_manufacturer",
                    models.CharField(
                        blank=True,
                        help_text="Transmission manufacturer of the equipment.",
                        max_length=50,
                        null=True,
                        verbose_name="Transmission Manufacturer",
                    ),
                ),
                (
                    "transmission_type",
                    models.CharField(
                        blank=True,
                        help_text="Transmission type of the equipment.",
                        max_length=50,
                        null=True,
                        verbose_name="Transmission Type",
                    ),
                ),
                (
                    "has_berth",
                    models.BooleanField(
                        default=False,
                        help_text="Equipment has Sleeper Berth.",
                        verbose_name="Has Berth",
                    ),
                ),
                (
                    "has_electronic_engine",
                    models.BooleanField(
                        default=False,
                        help_text="Equipment has Electronic Engine.",
                        verbose_name="Has Electronic Engine",
                    ),
                ),
                (
                    "highway_use_tax",
                    models.BooleanField(
                        default=False,
                        help_text="Equipment has Highway Use Tax.",
                        verbose_name="Highway Use Tax",
                    ),
                ),
                (
                    "owner_operated",
                    models.BooleanField(
                        default=False,
                        help_text="Equipment is Owner Operated.",
                        verbose_name="Owner Operated",
                    ),
                ),
                (
                    "ifta_qualified",
                    models.BooleanField(
                        default=False,
                        help_text="Equipment is IFTA Qualified.",
                        verbose_name="IFTA Qualified",
                    ),
                ),
                (
                    "equipment_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipment",
                        related_query_name="equipment",
                        to="equipment.equipmenttype",
                        verbose_name="Equipment Type",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipments",
                        related_query_name="equipment",
                        to="equipment.equipmentmanufacturer",
                        verbose_name="Manufacturer",
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
                "verbose_name": "Equipment",
                "verbose_name_plural": "Equipment",
                "ordering": ["id"],
            },
        ),
    ]