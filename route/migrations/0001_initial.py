# Generated by Django 4.1.3 on 2022-12-04 00:03

import uuid

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models

import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RouteControl",
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
                    "mileage_unit",
                    utils.models.ChoiceField(
                        choices=[("metric", "Metric"), ("imperial", "Imperial")],
                        default="imperial",
                        help_text="The mileage unit that the organization uses",
                        max_length=8,
                        verbose_name="Mileage Unit",
                    ),
                ),
                (
                    "traffic_model",
                    utils.models.ChoiceField(
                        choices=[
                            ("best_guess", "Best Guess"),
                            ("optimistic", "Optimistic"),
                            ("pessimistic", "Pessimistic"),
                        ],
                        default="best_guess",
                        help_text="The traffic model that the organization uses",
                        max_length=11,
                        verbose_name="Traffic Model",
                    ),
                ),
                (
                    "generate_routes",
                    models.BooleanField(
                        default=False,
                        help_text="Automatically generate routes for orders",
                        verbose_name="Generate Routes",
                    ),
                ),
                (
                    "avoid_tolls",
                    models.BooleanField(
                        default=True,
                        help_text="Avoid tolls when generating routes",
                        verbose_name="Avoid Tolls",
                    ),
                ),
                (
                    "avoid_highways",
                    models.BooleanField(
                        default=False,
                        help_text="Avoid highways when generating routes",
                        verbose_name="Avoid Highways",
                    ),
                ),
                (
                    "avoid_ferries",
                    models.BooleanField(
                        default=True,
                        help_text="Avoid ferries when generating routes",
                        verbose_name="Avoid Ferries",
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        help_text="Organization related to this route control",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="route_controls",
                        related_query_name="route_control",
                        to="organization.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Route Control",
                "verbose_name_plural": "Route Controls",
                "ordering": ("organization",),
            },
        ),
        migrations.CreateModel(
            name="Route",
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
                    "origin",
                    models.CharField(
                        blank=True,
                        help_text="Origin of the route",
                        max_length=255,
                        verbose_name="Origin",
                    ),
                ),
                (
                    "destination",
                    models.CharField(
                        blank=True,
                        help_text="Destination of the route",
                        max_length=255,
                        verbose_name="Destination",
                    ),
                ),
                (
                    "total_mileage",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Total Mile from origin to destination",
                        max_digits=10,
                        null=True,
                        verbose_name="Total Mileage",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Duration of route from origin to destination",
                        null=True,
                        verbose_name="Duration",
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
                "verbose_name": "Route",
                "verbose_name_plural": "Routes",
                "ordering": ("origin", "destination"),
            },
        ),
        migrations.AddIndex(
            model_name="route",
            index=models.Index(
                fields=["total_mileage", "duration"],
                name="route_route_total_m_60b843_idx",
            ),
        ),
    ]
