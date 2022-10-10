from rest_framework import serializers

from .models import Business


class BusinessListSerializer(serializers.ModelSerializer):
    """Use this serializer when you want to list Business model."""

    class Meta:
        model = Business
        fields = (
            "business_id",
            "name",
            "address",
            "city",
            "state",
            "postal_code",
            "latitude",
            "longitude",
            "stars",
            "review_count",
            "is_open",
        )
        read_only_fields = fields


class BusinessDetailSerializer(serializers.ModelSerializer):
    """Use this serializer when you want to get the detail of Business object."""

    class Meta:
        model = Business
        fields = (
            "business_id",
            "name",
            "address",
            "city",
            "state",
            "postal_code",
            "latitude",
            "longitude",
            "stars",
            "review_count",
            "is_open",
            "attributes",
            "categories",
            "hours",
        )
        read_only_fields = fields
