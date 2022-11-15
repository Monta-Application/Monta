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

from .models import Movement, Order
from .services import generation


@receiver(pre_save, sender=Order)
def generate_pro_number(sender: Order, instance: Order, **kwargs: Any) -> None:
    """Generate Pro Number
    Generate a pro number when a new order is added.
    Args:
        sender (Order): Order
        instance (Order): The order instance.
        **kwargs (Any): Keyword arguments.

    Returns:
        None
    """
    if not instance.pro_number:
        instance.pro_number = generation.OrderGenerationService.pro_number()


@receiver(pre_save, sender=Movement)
def generate_ref_number(sender: Movement, instance: Movement, **kwargs: Any) -> None:
    """Generate Reference Number

    Generate a reference number when a new movement is added.

    Args:
        sender (Movement): Movement
        instance (Movement): The movement instance.
        **kwargs (Any): Keyword arguments.

    Returns:
        None
    """
    if not instance.ref_num:
        instance.ref_num = generation.OrderGenerationService.movement_ref_number()
