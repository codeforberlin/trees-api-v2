from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import Tree


class TreeSerializer(gis_serializers.GeoFeatureModelSerializer):

    location = gis_serializers.GeometrySerializerMethodField()

    class Meta:
        model = Tree
        fields = ('id', 'location')
        geo_field = 'location'

    def get_location(self, obj):
        location = obj.location
        location.transform(4326)
        return location

    def get_properties(self, instance, fields):
        return instance.properties


class SpeciesSerializer(serializers.Serializer):

    species = serializers.CharField()
    count = serializers.IntegerField()


class GenusSerializer(serializers.Serializer):

    genus = serializers.CharField()
    count = serializers.IntegerField()


class BoroughSerializer(serializers.Serializer):

    borough = serializers.CharField()
    count = serializers.IntegerField()
