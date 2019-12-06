from django.core.management.base import BaseCommand, CommandError
from squirrel_project.models import Squirrel
import csv
import sys

class Command(BaseCommand):
    help = 'Export Squirrel Data in CSV format'

    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='+', help='Indicates file path.')

    def handle(self, *args, **kwargs):
        filepath = args[0]
        fields = Squirrel._meta.fields
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for obj in Squirrel.objects.all():
                row = []
                for field in fields:
                    row.append(getattr(obj, field.name))
                writer.writerow(row)



