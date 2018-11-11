from rest_framework_gis.pagination import GeoJsonPagination


class TreePagination(GeoJsonPagination):
    page_size = 10
    page_size_query_param = 'page_size'
