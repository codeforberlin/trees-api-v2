from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .models import Tree
from .serializers import TreeSerializer
from .paginations import TreePagination
from .filters import DistanceToPointFilter


class TreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    pagination_class = TreePagination

    filter_backends = (
        DistanceToPointFilter,
        DjangoFilterBackend
    )

    distance_filter_field = 'location'
    bbox_filter_field = 'location'

    bbox_filter_include_overlapping = True

    filter_fields = {
        'identifier': ['exact', 'contains'],
        'species': ['exact', 'contains'],
        'genus': ['exact', 'contains'],
        'borough': ['exact', 'contains'],
        'year': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'age': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'circumference': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'height': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'feature_name': ['exact'],
        'created': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'updated': ['exact', 'gt', 'lt', 'gte', 'lte'],
    }
