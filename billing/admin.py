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

from typing import Type

from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin[Customer]):
    """
    Customer Admin
    """

    model: Type[Customer] = Customer
    list_display = (
        "code",
        "name",
    )
    search_fields = ("code", "name")
    autocomplete_fields = ("organization",)

    def get_queryset(self, request):
        """
        Get Queryset
        """
        return super().get_queryset(request).filter(organization=request.user.profile.organization)

    def save_model(self, request, obj, form, change):
        """
        Save Model
        """
        obj.organization = request.user.profile.organization
        super().save_model(request, obj, form, change)