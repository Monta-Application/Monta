# -*- coding: utf-8 -*-
# Generated by Django 4.1.2 on 2022-11-02 05:51

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organization", "0006_alter_depotdetail_address_line_1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderControl",
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
                    "auto_rate_orders",
                    models.BooleanField(
                        default=True,
                        help_text="Auto rate orders",
                        verbose_name="Auto Rate",
                    ),
                ),
                (
                    "calculate_distance",
                    models.BooleanField(
                        default=True,
                        help_text="Calculate distance for the order",
                        verbose_name="Calculate Distance",
                    ),
                ),
                (
                    "enforce_bill_to",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce bill to to being enter when entering an order.",
                        verbose_name="Enforce Bill To",
                    ),
                ),
                (
                    "enforce_rev_code",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce rev code code being entered when entering an order.",
                        verbose_name="Enforce Rev Code",
                    ),
                ),
                (
                    "enforce_shipper",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce shipper when putting in an order.",
                        verbose_name="Enforce Shipper",
                    ),
                ),
                (
                    "enforce_cancel_comm",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce comment when cancelling an order.",
                        verbose_name="Enforce Voided Comm",
                    ),
                ),
                (
                    "generate_routes",
                    models.BooleanField(
                        default=False,
                        help_text="Generate routes for the organization",
                        verbose_name="Generate Routes",
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_control",
                        related_query_name="order_controls",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order Control",
                "verbose_name_plural": "Order Controls",
                "ordering": ["organization"],
            },
        ),
        migrations.CreateModel(
            name="GoogleAPI",
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
                    "api_key",
                    models.CharField(
                        help_text="Google API Key for the organization.",
                        max_length=255,
                        verbose_name="API Key",
                    ),
                ),
                (
                    "mileage_unit",
                    models.CharField(
                        choices=[("metric", "Metric"), ("imperial", "Imperial")],
                        default="imperial",
                        help_text="The mileage unit that the organization uses",
                        max_length=255,
                        verbose_name="Mileage Unit",
                    ),
                ),
                (
                    "traffic_model",
                    models.CharField(
                        choices=[
                            ("best_guess", "Best Guess"),
                            ("optimistic", "Optimistic"),
                            ("pessimistic", "Pessimistic"),
                        ],
                        default="best_guess",
                        help_text="The traffic model that the organization uses",
                        max_length=255,
                        verbose_name="Traffic Model",
                    ),
                ),
                (
                    "add_customer_location",
                    models.BooleanField(
                        default=False,
                        help_text="Add customer location through google places",
                        verbose_name="Add Customer Location",
                    ),
                ),
                (
                    "add_location",
                    models.BooleanField(
                        default=False,
                        help_text="Add location through google places",
                        verbose_name="Add Location",
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="google_api",
                        related_query_name="google_apis",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Google API",
                "verbose_name_plural": "Google APIs",
                "ordering": ["organization"],
            },
        ),
        migrations.CreateModel(
            name="DispatchControl",
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
                    "record_service_incident",
                    models.CharField(
                        choices=[
                            ("Never", "Never"),
                            ("Pickup", "Pickup"),
                            ("Delivery", "Delivery"),
                            ("Pickup and Delivery", "Pickup and Delivery"),
                            ("All except shipper", "All except shipper"),
                        ],
                        default="Never",
                        max_length=19,
                        verbose_name="Record Service Incident",
                    ),
                ),
                (
                    "grace_period",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Grace period for the service incident in minutes.",
                        verbose_name="Grace Period",
                    ),
                ),
                (
                    "deadhead_target",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Deadhead Mileage target for the company.",
                        max_digits=5,
                        verbose_name="Deadhead Target",
                    ),
                ),
                (
                    "driver_assign",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce driver assign for the company.",
                        verbose_name="Enforce Driver Assign",
                    ),
                ),
                (
                    "trailer_continuity",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce trailer continuity for the company.",
                        verbose_name="Enforce Trailer Continuity",
                    ),
                ),
                (
                    "distance_method",
                    models.CharField(
                        choices=[("Google", "Google"), ("Monta", "Monta")],
                        default="Monta",
                        help_text="Distance method for the company.",
                        max_length=20,
                        verbose_name="Distance Method",
                    ),
                ),
                (
                    "dupe_trailer_check",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce duplicate trailer check for the company.",
                        verbose_name="Enforce Duplicate Trailer Check",
                    ),
                ),
                (
                    "regulatory_check",
                    models.BooleanField(
                        default=False,
                        help_text="Enforce regulatory check for the company.",
                        verbose_name="Enforce Regulatory Check",
                    ),
                ),
                (
                    "prev_orders_on_hold",
                    models.BooleanField(
                        default=False,
                        help_text="Prevent dispatch of orders on hold for the company.",
                        verbose_name="Prevent Orders On Hold",
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dispatch_control",
                        related_query_name="dispatch_controls",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dispatch Control",
                "verbose_name_plural": "Dispatch Controls",
                "ordering": ["organization"],
            },
        ),
    ]