from rest_framework import pagination

from rest_framework_gis import pagination as gis_pagination


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class GeoJsonPagination(gis_pagination.GeoJsonPagination):
    page_size = 10
    page_size_query_param = 'page_size'
