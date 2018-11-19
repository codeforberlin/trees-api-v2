from django.db.models import Count

from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .models import Tree
from .paginations import PageNumberPagination, GeoJsonPagination
from .filters import DistanceToPointFilter
from .serializers import (
    TreeSerializer,
    SpeciesSerializer,
    GenusSerializer,
    BoroughSerializer
)


class TreeViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    pagination_class = GeoJsonPagination

    filter_backends = (
        DistanceToPointFilter,
        DjangoFilterBackend
    )

    distance_filter_field = 'location'
    bbox_filter_field = 'location'

    bbox_filter_include_overlapping = True

    filter_fields = {
        'identifier': ['exact', 'iexact', 'contains'],
        'species': ['exact', 'iexact', 'contains'],
        'genus': ['exact', 'iexact', 'contains'],
        'borough': ['exact', 'iexact', 'contains'],
        'year': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'age': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'circumference': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'height': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'feature_name': ['exact'],
        'created': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'updated': ['exact', 'gt', 'lt', 'gte', 'lte'],
    }


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = SpeciesSerializer
    pagination_class = PageNumberPagination

    filter_backends = (DjangoFilterBackend, )

    filter_fields = {
        'species': ['exact', 'iexact', 'contains']
    }

    def get_queryset(self):
        return Tree.objects.all().values('species').annotate(count=Count('species')).order_by('-count')


class GenusViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GenusSerializer
    pagination_class = PageNumberPagination

    filter_backends = (DjangoFilterBackend, )

    filter_fields = {
        'genus': ['exact', 'iexact', 'contains']
    }

    def get_queryset(self):
        return Tree.objects.all().values('genus').annotate(count=Count('genus')).order_by('-count')


class BoroughViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = BoroughSerializer
    pagination_class = PageNumberPagination

    filter_backends = (DjangoFilterBackend, )

    filter_fields = {
        'borough': ['exact', 'iexact', 'contains']
    }

    def get_queryset(self):
        return Tree.objects.all().values('borough').annotate(count=Count('borough')).order_by('-count')
