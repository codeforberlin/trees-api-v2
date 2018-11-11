from django.contrib.gis.db import models


class Tree(models.Model):

    location = models.PointField(srid=25833)

    identifier = models.CharField(max_length=256, null=True, blank=True, db_index=True)
    species = models.CharField(max_length=256, null=True, blank=True, db_index=True)
    genus = models.CharField(max_length=256, null=True, blank=True, db_index=True)
    borough = models.CharField(max_length=256, null=True, blank=True, db_index=True)

    year = models.IntegerField(null=True, db_index=True)
    age = models.IntegerField(null=True, db_index=True)
    circumference = models.IntegerField(null=True, db_index=True)
    height = models.IntegerField(null=True, db_index=True)

    feature_name = models.CharField(max_length=64, db_index=True)

    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return str(self.location)

    @property
    def properties(self):
        return {
            'identifier': self.identifier,
            'species': self.species,
            'genus': self.genus,
            'borough': self.borough,
            'year': self.year,
            'age': self.age,
            'circumference': self.circumference,
            'height': self.height,
            'feature_name': self.feature_name,
            'created': self.created,
            'updated': self.updated
        }
