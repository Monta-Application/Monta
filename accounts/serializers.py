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

from typing import Any, OrderedDict

from rest_framework import serializers

from accounts import models
from utils.serailizers import ValidatedSerializer


class VerifyTokenSerializer(serializers.Serializer):
    """
    Verify Token Serializer
    """

    token = serializers.CharField()

    def validate(self, attrs: OrderedDict[str, Any]) -> dict[str, Any]:
        """Validate the token

        Args:
            attrs (OrderedDict): Attributes

        Returns:
            dict[str, Any]: Validated attributes
        """

        token = attrs.get("token")

        if models.Token.objects.filter(key=token).exists():
            # Query the user from the token and return the ID of the user
            return {
                "token": token,
                "user_id": models.Token.objects.get(key=token).user.id,
            }
        else:
            msg = "Unable to validate given token"
            raise serializers.ValidationError(msg, code="authentication")


class UserProfileSerializer(ValidatedSerializer):
    """
    User Profile Serializer
    """

    class Meta:
        """
        Metaclass for UserProfileSerializer
        """

        model = models.UserProfile
        fields = [
            "user",
            "first_name",
            "last_name",
            "title",
            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "zip_code",
            "phone",
        ]


class UserSerializer(ValidatedSerializer):
    """
    User Serializer
    """

    password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer(required=False)

    class Meta:
        """
        Metaclass for UserSerializer
        """

        model = models.User
        fields = (
            "id",
            "organization",
            "department",
            "username",
            "password",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "profile",
        )


class TokenSerializer(ValidatedSerializer):
    """
    Serializer for Token model
    """

    key = serializers.CharField(
        min_length=40, max_length=40, allow_blank=True, required=False
    )
    user = UserSerializer()

    class Meta:
        """
        Metaclass for TokenSerializer
        """

        model: type[models.Token] = models.Token
        fields = ["id", "user", "created", "expires", "last_used", "key", "description"]


class TokenProvisionSerializer(serializers.Serializer):
    """
    Token Provision Serializer
    """

    username = serializers.CharField()
    password = serializers.CharField()
