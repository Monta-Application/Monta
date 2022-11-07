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

from typing import Any

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Customer


@receiver(pre_save, sender=Customer)
def generate_worker_code(sender: Customer, instance: Customer, **kwargs: Any) -> None:
    """Generate Customer Code

    Generate a customer code when a new worker is added.

    Args:
        sender (Customer): Customer
        instance (Customer): The customer instance.
        **kwargs (Any): Keyword arguments.

    Returns:
        None
    """
    if not instance.code:
        instance.code = Customer.generate_customer_code(instance)