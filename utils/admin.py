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

from typing import Any, Sequence, TypeVar

from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Model, QuerySet
from django.forms import BaseModelForm
from django.forms.models import ModelForm
from django.http import HttpRequest

# Model Generic Type
_M = TypeVar("_M", bound=Model)

# Child Model Generic Type
_C = TypeVar("_C", bound=Model)

# Parent Model Generic Type
_P = TypeVar("_P", bound=Model)


class GenericAdmin(admin.ModelAdmin[_M]):
    """
    Generic Admin Class for all models
    """

    autocomplete: bool = True
    exclude: tuple[str, ...] = ("organization",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[_M]:
        """Get Queryset for Model
        Args:
            request (HttpRequest): Request Object
        Returns:
            QuerySet[Model]: Queryset of Model
        """
        return (
            super()
            .get_queryset(request)
            .select_related(*self.get_autocomplete_fields(request))
            .filter(organization=request.user.organization)  # type: ignore
        )

    def save_model(
            self,
            request: HttpRequest,
            obj: _M,
            form: type[BaseModelForm],
            change: bool,
    ) -> None:
        """Save Model Instance
        Args:
            request (HttpRequest): Request Object
            obj (_M): Generic Model Object
            form (Type[BaseModelForm]): Form Class
            change (bool): If the model is being changed
        Returns:
            None
        """
        obj.organization = request.user.organization  # type: ignore
        super().save_model(request, obj, form, change)

    def save_formset(
            self, request: HttpRequest, form: Any, formset: Any, change: Any
    ) -> None:
        """Save Formset for Inline Models
        Args:
            request (HttpRequest): Request Object
            form (Any): Form Object
            formset (Any): Formset Object
            change (Any): If the model is being changed
        Returns:
            None
        """
        instances = formset.save(commit=False)
        for instance in instances:
            instance.organization = request.user.organization  # type: ignore
            instance.save()
        formset.save_m2m()
        super().save_formset(request, form, formset, change)

    def get_form(
            self,
            request: HttpRequest,
            obj: _M | None = None,
            change: bool = False,
            **kwargs: Any,
    ) -> type[ModelForm[_M]]:
        """Get Form for Model
        Args:
            change (bool): If the model is being changed
            request (HttpRequest): Request Object
            obj (Optional[_M]): Model Object
            **kwargs (Any): Keyword Arguments
        Returns:
            Type[ModelForm[Any]]: Form Class
        """
        form = super().get_form(request, obj, **kwargs)
        for field in form.base_fields:
            print(field)
            if field == "organization":
                form.base_fields[field].initial = request.user.organization  # type: ignore
                form.base_fields[field].widget = form.base_fields[field].hidden_widget()
            form.base_fields[field].widget.attrs["placeholder"] = field.title()
        return form

    def get_autocomplete_fields(self, request: HttpRequest) -> Sequence[str]:
        """Get Autocomplete Fields
        Args:
            request (HttpRequest): Request Object
        Returns:
            Sequence[str]: Autocomplete Fields
        """
        if self.autocomplete:
            if not self.search_fields:
                raise ImproperlyConfigured(
                    f"{self.__class__.__name__} must define search_fields"
                    " when self.autocomplete is True"
                )

            autocomplete_fields = []
            for field in self.model._meta.get_fields():
                if field.is_relation and field.many_to_one:
                    autocomplete_fields.append(field.name)
            return autocomplete_fields
        return []


class GenericStackedInline(admin.StackedInline[_C, _P]):
    """
    Generic Admin Stacked for all Models with Organization Exclusion
    """

    extra = 0

    def get_queryset(self, request: HttpRequest) -> QuerySet[_C]:
        """Get Queryset
        Args:
            request (HttpRequest): Request Object
        Returns:
            QuerySet[_C]: Queryset of Model
        """
        return (
            super()
            .get_queryset(request)
            .select_related(*self.get_autocomplete_fields(request))
            .filter(organization=request.user.organization)  # type: ignore
        )

    def get_autocomplete_fields(self, request: HttpRequest) -> Sequence[str]:
        """Get Autocomplete Fields
        Returns:
            Sequence[str]: Autocomplete Fields
        """
        autocomplete_fields = []
        for field in self.model._meta.get_fields():
            if field.is_relation and field.many_to_one:
                autocomplete_fields.append(field.name)
        return autocomplete_fields


class GenericTabularInline(GenericStackedInline[_C, _P]):
    """
    Generic Admin Tabular Inline with Organization Exclusion
    """

    template = "admin/edit_inline/tabular.html"
