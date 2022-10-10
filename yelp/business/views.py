from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Business
from .serializers import BusinessListSerializer, BusinessDetailSerializer
from review.serializers import ReviewListSerializer


# Create your views here.
class BusinessViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Business.objects.all()
    serializer_class = BusinessListSerializer
    max_page_size = 1000
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
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
    ]
    ordering = ["-stars"]

    def get_serializer_class(self):
        if self.action in ["retrieve"]:
            self.serializer_class = BusinessDetailSerializer
        return super().get_serializer_class()

    def reviews_response(self, reviews):
        page = self.paginate_queryset(reviews)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    def chose_orde_by(self, queryset, order_by: str):
        if order_by == "stars":
            return queryset.order_by("stars")
        if order_by == "-stars":
            return queryset.order_by("-stars")
        if order_by == "useful":
            return queryset.order_by("useful")
        if order_by == "-useful":
            return queryset.order_by("-useful")
        if order_by == "funny":
            return queryset.order_by("funny")
        if order_by == "-funny":
            return queryset.order_by("-funny")
        if order_by == "cool":
            return queryset.order_by("cool")
        if order_by == "-cool":
            return queryset.order_by("-cool")

    @action(detail=True, serializer_class=ReviewListSerializer)
    def reviews(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        reviews = instance.reviews.all()
        ordering = request.query_params.get("ordering")
        if ordering:
            reviews = self.chose_orde_by(reviews, ordering)
        else:
            reviews = reviews.order_by("-date")
        return self.reviews_response(reviews=reviews)
