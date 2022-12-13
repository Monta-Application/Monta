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
            name="DocumentClassification",
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
                        help_text="Document classification name",
                        max_length=150,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Document classification description",
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
                "verbose_name": "Document Classification",
                "verbose_name_plural": "Document Classifications",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="ChargeType",
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
                    models.CharField(max_length=50, unique=True, verbose_name="Name"),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Description"
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
                "verbose_name": "Charge Type",
                "verbose_name_plural": "Charge Types",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="AccessorialCharge",
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
                    "code",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Code",
                    ),
                ),
                (
                    "is_detention",
                    models.BooleanField(default=False, verbose_name="Is Detention"),
                ),
                (
                    "charge_amount",
                    models.DecimalField(
                        decimal_places=2,
                        default=1.0,
                        help_text="Charge Amount",
                        max_digits=10,
                        verbose_name="Charge Amount",
                    ),
                ),
                (
                    "method",
                    utils.models.ChoiceField(
                        choices=[("D", "Distance"), ("F", "Flat"), ("P", "Percentage")],
                        default="D",
                        max_length=1,
                        verbose_name="Method",
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
                "verbose_name": "Other Charge",
                "verbose_name_plural": "Other Charges",
                "ordering": ["code"],
            },
        ),
    ]
