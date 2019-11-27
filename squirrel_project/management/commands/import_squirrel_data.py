from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from squirrel_project.models import Squirrel
import csv
import os

class Command(BaseCommand):
    help = 'Import Squirrel Data. File path should be passed.'
    
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*', type = str, help='Indicates the file path')
    
    def handle(self, *args, **kwargs):
        filepath = args[0]
        with open(filepath) as squirrel_data:
            reader = csv.reader(squirrel_data)
            header = squirrel_data.readline().strip().split(',')
            fields = [field.lower().replace(' ','_').replace('/','_') for field in header]
            for row in reader:
                obj = Squirrel()
                for col_num, value in enumerate(row):
                    if value == 'true':
                        value  = True
                    if value == 'false':
                        value = False
                    if col_num == 5:
                        value = value[4:]+'-'+value[:2]+'-'+value[2:4]
                    
                    setattr(obj, fields[col_num], value)
                obj.save()


