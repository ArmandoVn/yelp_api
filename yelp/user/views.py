from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.schemas.openapi import SchemaGenerator
from rest_framework.schemas.openapi import AutoSchema

from .models import YelpUser
from .serializers import YelpUserListSerializer


# Create your views here.
class YelpUserViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = YelpUser.objects.all()
    serializer_class = YelpUserListSerializer
    max_page_size = 1000
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'name', 
        'review_count', 
        'yelping_since', 
        'useful', 
        'funny', 
        'cool', 
        'fans', 
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
    ]
    ordering = ['-average_stars']
    schema = AutoSchema(
        tags=['Pets'],
        component_name='Pet',
        operation_id_base='Pet',
    )

