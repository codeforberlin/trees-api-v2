import logging
import requests
import yaml

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('config', help='the config file for the feature')

    def handle(self, *args, **options):
        with open(options['config']) as f:
            config = yaml.load(f.read())

        response = requests.get(config['url'], stream=True)

        with open(config['file_name'], 'wb') as f:
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
