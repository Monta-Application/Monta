# -*- coding: utf-8 -*-
"""
COPYRIGHT 2022 MONTA

This file is part of Monta.

Monta is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Monta is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Monta.  If not, see <https://www.gnu.org/licenses/>.
"""

from __future__ import annotations

from typing import Any, Optional

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from localflavor.us.models import USStateField, USZipCodeField

from organization.models import Organization


class UserManager(BaseUserManager):
    """
    Base user manager
    """

    def create_user(
        self,
        user_name: str,
        email: str,
        password: str | None = None,
        **extra_fields: Any,
    ) -> User:
        """
        Create and save a user with the given email and password.

        Args:
            user_name (str):
            email (str):
            password (str | None, optional): Password for the user. Defaults to None.
            **extra_fields (Any):

        Returns: User

        """
        if not user_name:
            raise ValueError(_("The username must be set"))
        if not email:
            raise ValueError(_("The email must be set"))

        user = self.model(
            username=user_name.lower(),
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """

    username = models.CharField(
        _("Username"),
        max_length=30,
        unique=True,
        help_text=_(
            "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    email = models.EmailField(
        _("Email Address"),
        unique=True,
        help_text=_("Required. A valid email address."),
    )
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: list[str] = ["email"]

    class Meta:
        """
        Metaclass for the User Model
        """

        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering: list[str] = ["-date_joined"]

    def __str__(self) -> str:
        """
        Returns (str): String representation of the User
        """
        return self.username

    def get_absolute_url(self) -> str:
        """
        Returns (str): Get the absolute url of the User
        """
        return reverse("users:detail", kwargs={"pk": self.pk})


class Profile(TimeStampedModel):
    """
    Profile Model
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="profiles",
        related_query_name="profile",
        verbose_name=_("User"),
    )
    organization = models.ForeignKey(
        "Organization",
        on_delete=models.PROTECT,
        related_name="profiles",
        related_query_name="profile",
        verbose_name=_("Organization"),
    )
    title = models.ForeignKey(
        "JobTitle",
        on_delete=models.PROTECT,
        related_name="profiles",
        related_query_name="profile",
        verbose_name=_("Job Title"),
    )
    first_name = models.CharField(
        _("First Name"),
        max_length=255,
        help_text=_("The first name of the user"),
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=255,
        help_text=_("The last name of the user"),
    )
    profile_picture = models.ImageField(
        _("Profile Picture"),
        upload_to="profiles/",
        null=True,
        blank=True,
        help_text=_("The profile picture of the user"),
    )
    bio = models.TextField(
        _("Bio"),
        null=True,
        blank=True,
        help_text=_("The bio of the user"),
    )
    address_line_1 = models.CharField(
        _("Address"),
        max_length=100,
        help_text=_("The address of the user"),
    )
    address_line_2 = models.CharField(
        _("Address Line 2"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("The address of the user"),
    )
    city = models.CharField(
        _("City"),
        max_length=100,
        help_text=_("The city of the user"),
    )
    state = USStateField(
        _("State"),
        help_text=_("Enter the state of the user"),
    )
    zip_code = USZipCodeField(
        _("Zip Code"),
        help_text=_("Enter the zip code of the user"),
    )
    phone = models.CharField(
        _("Phone Number"),
        max_length=15,
        null=True,
        blank=True,
        help_text=_("The phone number of the user"),
    )
    email_verified = models.BooleanField(
        _("Email Verified"),
        default=False,
        help_text=_("If the user has verified their email"),
    )

    class Meta:
        """
        Metaclass for the Profile model
        """

        ordering: list[str] = ["-created"]
        verbose_name: str = _("Profile")
        verbose_name_plural: str = _("Profiles")
        indexes: list[models.Index] = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self) -> str:
        """
        Returns (str): String representation of the Profile Model
        """
        return str(self.user.username)

    def get_absolute_url(self) -> str:
        """
        Returns (str): Get the absolute url of the profile
        """
        return reverse("user:profile-view", kwargs={"pk": self.pk})

    def get_user_profile_pic(self) -> str:
        """
        Returns (str): Get the profile picture of the user
        """
        if self.profile_picture:
            return str(self.profile_picture)
        return "/static/media/avatars/blank.avif"

    def get_user_city_state(self) -> Optional[str]:
        """
        Returns (str): Get the city and state of the user
        """
        if self.city and self.state:
            return f"{self.city}, {self.state}"
        return None

    def get_full_name(self) -> str:
        """
        Returns (str): Get the full name of the user
        """
        return f"{self.first_name} {self.last_name}"


class JobTitle(TimeStampedModel):
    """
    Job Title Model Fields
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="job_titles",
        related_query_name="job_title",
        verbose_name=_("Organization"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        unique=True,
        help_text=_("Name of the job title"),
    )
    description = models.TextField(
        _("Description"),
        null=True,
        blank=True,
        help_text=_("Description of the job title"),
    )

    class Meta:
        """
        Metaclass for the JobTitle model
        """

        verbose_name = _("Job Title")
        verbose_name_plural = _("Job Titles")
        ordering: list[str] = ["name"]
        indexes: list[models.Index] = [
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        """
        Returns (str): String representation of the JobTitle model
        """
        return str(self.name)

    def get_absolute_url(self) -> str:
        """
        Returns (str): Get the absolute url of the job title
        """
        return reverse("user:job-title-view", kwargs={"pk": self.pk})
