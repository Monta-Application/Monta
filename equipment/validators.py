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

import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def us_vin_number_validator(value: str) -> None:
    """Validate US VIN number.

    Args:
        value (str): Input value

    Returns:
        None: If value is valid
    """
    if not re.match(r"^(?=.*[0-9])(?=.*[A-z])[0-9A-z-]{17}$", value):
        raise ValidationError(
            _("%(value)s is not a valid US VIN number. Please try again."),
            params={"value": value},
        )
