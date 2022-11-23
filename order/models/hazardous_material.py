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

# THIS FILE IS A FUCKING NIGHTMARE BUT PYTHON & FUCKING DJANGO!

from __future__ import annotations

import textwrap
from typing import final

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from utils.models import ChoiceField, GenericModel


class HazardousMaterial(GenericModel):
    """
    Hazardous Class Model Fields that can be used in the
    :model:`order.Order` & :model:`order.Commodity` model.
    """

    @final
    class HazardousClassChoices(models.TextChoices):
        """
        Status choices for Order model
        """

        CLASS_1_1 = "1.1", _("Division 1.1: Mass Explosive Hazard")
        CLASS_1_2 = "1.2", _("Division 1.2: Projection Hazard")
        CLASS_1_3 = "1.3", _(
            "Division 1.3: Fire and/or Minor Blast/Minor Projection Hazard"
        )
        CLASS_1_4 = "1.4", _("Division 1.4: Minor Explosion Hazard")
        CLASS_1_5 = "1.5", _(
            "Division 1.5: Very Insensitive With Mass Explosion Hazard"
        )
        CLASS_1_6 = "1.6", _(
            "Division 1.6: Extremely Insensitive; No Mass Explosion Hazard"
        )
        CLASS_2_1 = "2.1", _("Division 2.1: Flammable Gases")
        CLASS_2_2 = "2.2", _("Division 2.2: Non-Flammable Gases")
        CLASS_2_3 = "2.3", _("Division 2.3: Poisonous Gases")
        CLASS_3 = "3", _("Division 3: Flammable Liquids")
        CLASS_4_1 = "4.1", _("Division 4.1: Flammable Solids")
        CLASS_4_2 = "4.2", _("Division 4.2: Spontaneously Combustible Solids")
        CLASS_4_3 = "4.3", _("Division 4.3: Dangerous When Wet")
        CLASS_5_1 = "5.1", _("Division 5.1: Oxidizing Substances")
        CLASS_5_2 = "5.2", _("Division 5.2: Organic Peroxides")
        CLASS_6_1 = "6.1", _("Division 6.1: Toxic Substances")
        CLASS_6_2 = "6.2", _("Division 6.2: Infectious Substances")
        CLASS_7 = "7", _("Division 7: Radioactive Material")
        CLASS_8 = "8", _("Division 8: Corrosive Substances")
        CLASS_9 = "9", _("Division 9: Miscellaneous Hazardous Substances and Articles")

    @final
    class PackingGroupChoices(models.TextChoices):
        """
        Status choices for Order model
        """

        ONE = "I", _("I")
        TWO = "II", _("II")
        THREE = "III", _("III")

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
    )
    name = models.CharField(
        _("Name"),
        max_length=255,
        unique=True,
        help_text=_("Name of the Hazardous Class"),
    )
    description = models.TextField(
        _("Description"),
        blank=True,
        help_text=_("Description of the Hazardous Class"),
    )
    hazard_class = ChoiceField(
        _("Hazard Class"),
        choices=HazardousClassChoices.choices,
        help_text=_("Hazard Class of the Hazardous Material"),
    )
    packing_group = ChoiceField(
        _("Packing Group"),
        choices=PackingGroupChoices.choices,
        help_text=_("Packing Group of the Hazardous Material"),
        blank=True,
    )
    erg_number = models.CharField(
        _("ERG Number"),
        max_length=255,
        blank=True,
    )
    proper_shipping_name = models.TextField(
        _("Proper Shipping Name"),
        help_text=_("Proper Shipping Name of the Hazardous Material"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Hazardous Material")
        verbose_name_plural = _("Hazardous Materials")
        ordering: list[str] = ["name"]

    def __str__(self) -> str:
        """Hazardous Material String Representation

        Returns:
            str: Hazardous Material Name
        """
        return textwrap.wrap(self.name, 50)[0]

    def get_absolute_url(self) -> str:
        """Hazardous Material Absolute URL

        Returns:
            str: Hazardous Material Absolute URL
        """
        return reverse("order:hazardousmaterial_detail", kwargs={"pk": self.pk})