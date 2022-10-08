from rest_framework import serializers

from .models import Business

class BusinessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            'business_id',
            'name',
            'address',
            'city',
            'state',
            'postal_code',
            'latitude',
            'longitude',
            'stars',
            'review_count',
            'is_open',
        )
        read_only_fields = fields
    
class BusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            'business_id',
            'name',
            'address',
            'city',
            'state',
            'postal_code',
            'latitude',
            'longitude',
            'stars',
            'review_count',
            'is_open',
            'attributes',
            'categories',
            'hours',
        )
        read_only_fields = fields