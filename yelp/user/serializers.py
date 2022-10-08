from rest_framework import serializers

from .models import YelpUser

class YelpUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpUser
        fields = (
            'user_id',
            'name',
            'review_count',
            'yelping_since',
            'useful',
            'funny',
            'cool',
            'fans',
            'elite',
            'average_stars',
            'compliment_hot',
            'compliment_more',
            'compliment_profile',
            'compliment_cute',
            'compliment_list',
            'compliment_note',
            'compliment_plain',
            'compliment_cool',
            'compliment_funny',
            'compliment_writer',
            'compliment_photos',
        )
        read_only_fields = fields
    
class YelpUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpUser
        fields = (
            'user_id',
            'name',
            'review_count',
            'yelping_since',
            'useful',
            'funny',
            'cool',
            'fans',
            'friends',
            'elite',
            'average_stars',
            'compliment_hot',
            'compliment_more',
            'compliment_profile',
            'compliment_cute',
            'compliment_list',
            'compliment_note',
            'compliment_plain',
            'compliment_cool',
            'compliment_funny',
            'compliment_writer',
            'compliment_photos',
        )
        read_only_fields = fields