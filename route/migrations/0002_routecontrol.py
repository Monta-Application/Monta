# -*- coding: utf-8 -*-
# Generated by Django 4.1.2 on 2022-11-06 22:10

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0006_alter_depotdetail_address_line_1_and_more"),
        ("route", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RouteControl",
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
                        related_name="route_control",
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
    ]