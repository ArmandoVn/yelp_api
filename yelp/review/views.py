from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewListSerializer
from review.serializers import ReviewListSerializer


# Create your views here.
class ReviewViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    max_page_size = 1000
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'stars',
        'useful',
        'funny',
        'cool',
        'text',
        'date',
    ]
    ordering = ['-stars']
