from django.contrib.gis.geos import Point

from rest_framework.exceptions import ParseError
from rest_framework_gis import filters as gis_filters


class DistanceToPointFilter(gis_filters.DistanceToPointFilter):

    def get_filter_point(self, request):
        point_string = request.query_params.get(self.point_param, None)

        if not point_string:
            return None

        try:
            (x, y) = (float(n) for n in point_string.split(','))
        except ValueError:
            raise ParseError('Invalid geometry string supplied for parameter {0}'.format(self.point_param))

        p = Point(x, y, srid=4326)
        p.transform(25833)

        return p
