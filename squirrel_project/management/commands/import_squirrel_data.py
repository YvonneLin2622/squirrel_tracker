from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from squirrel_project.models import Squirrel
import csv
import os

class Command(BaseCommand):
    help = 'Import Squirrel Data. File path should be passed.'
    
    def add_arguments(self, parser):
        parser.add_argument('file path', nargs='*', type = str, help='Indicates the file path')
    
    def handle(self, *args, **kwargs):
        filepath = args[0]


