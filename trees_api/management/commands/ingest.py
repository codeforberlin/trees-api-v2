import logging
import xml.sax
import yaml

from collections import Counter
from tqdm import tqdm
from dateutil import parser

from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from django.utils.timezone import get_current_timezone

from trees_api.models import Tree

logger = logging.getLogger(__name__)


class TimeStampHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        if name == 'wfs:FeatureCollection':
            tz = get_current_timezone()
            naive_time_stamp = parser.parse(attrs.get('timeStamp'))
            self.time_stamp = tz.localize(naive_time_stamp)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('config', help='the config file for the feature')
        parser.add_argument('--dry', action='store_true', help='perform a dry run')

    def handle(self, *args, **options):
        with open(options['config']) as f:
            config = yaml.safe_load(f.read())

        # get the timeStamp using a SAX parser
        handler = TimeStampHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        with open(config['file_name']) as f:
            parser.parse(f)

        time_stamp = handler.time_stamp

        data_source = DataSource(config['file_name'])

        counter = Counter()

        for feature in tqdm(data_source[0]):
            # parse the point from the point in the feature
            point = GEOSGeometry(str(feature.geom), srid=25833)

            try:
                tree = Tree.objects.get(location=point)
                counter['updated'] += 1
            except Tree.DoesNotExist:
                tree = Tree(location=point, created=time_stamp)
                counter['created'] += 1

            for attr in ['identifier', 'species', 'genus', 'borough']:
                key = config['fields'].get(attr)
                if key:
                    value = feature[key].value
                    setattr(tree, attr, value)

            for attr in ['year', 'age', 'circumference', 'height']:
                key = config['fields'].get(attr)
                if key:
                    value = feature[key].value
                    setattr(tree, attr, value)

            tree.feature_name = config['feature_name']
            tree.updated = time_stamp

            if options['dry']:
                print(tree, tree.properties)
            else:
                tree.save()

        print(counter)
