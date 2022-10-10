from rest_framework import serializers

from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    """Use this serializer when you want to list Review model."""

    class Meta:
        model = Review
        fields = (
            "review_id",
            "business_id",
            "user_id",
            "stars",
            "useful",
            "funny",
            "cool",
            "text",
            "date",
        )
        read_only_fields = fields


class ReviewDetailSerializer(serializers.ModelSerializer):
    """Use this serializer when you want to get the detail of Review object."""

    class Meta:
        model = Review
        fields = (
            "review_id",
            "stars",
            "useful",
            "funny",
            "cool",
            "text",
            "date",
        )
        read_only_fields = fields
