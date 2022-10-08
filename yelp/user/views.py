from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import YelpUser
from .serializers import YelpUserListSerializer, YelpUserDetailSerializer
from review.serializers import ReviewListSerializer


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

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            self.serializer_class = YelpUserDetailSerializer
        return super().get_serializer_class()

    def reviews_response(self, reviews):
        page = self.paginate_queryset(reviews)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    def chose_orde_by(self, queryset, order_by: str):
        if order_by == 'stars':
            return queryset.order_by('stars')
        if order_by == '-stars':
            return queryset.order_by('-stars')
        if order_by == 'useful':
            return queryset.order_by('useful')
        if order_by == '-useful':
            return queryset.order_by('-useful')
        if order_by == 'funny':
            return queryset.order_by('funny')
        if order_by == '-funny':
            return queryset.order_by('-funny')
        if order_by == 'cool':
            return queryset.order_by('cool')
        if order_by == '-cool':
            return queryset.order_by('-cool')

    @action(detail=True, serializer_class=ReviewListSerializer)
    def reviews(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        reviews = instance.reviews.all()
        ordering = request.query_params.get('ordering')
        if ordering:
            reviews = self.chose_orde_by(reviews, ordering)
        else:
            reviews = reviews.order_by('-date')
        return self.reviews_response(reviews=reviews)