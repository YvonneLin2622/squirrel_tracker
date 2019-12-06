from django.core.management.base import BaseCommand, CommandError
from squirrel_project.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Import Squirrel Data. File path should be passed.'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            date = item['Date']
            string = [item['Running'],item['Chasing'],item['Climbing'],item['Eating'],item['Foraging'],
                    item['Kuks'], item['Quaas'],item['Moans'],item['Tail flags'],item['Tail twitches'],
                    item['Approaches'], item['Indifferent'], item['Runs from']]
            b = [True if val == 'true' else False for val in string]
            s = Squirrel(
                   x = item['X'],
                   y = item['Y'],
                   unique_squirrel_id = item['Unique Squirrel ID'],
                   shift = item['Shift'],
                   date = date[4:]+'-'+date[:2]+'-'+date[2:4],
                   age = item['Age'],
                   primary_fur_color = item['Primary Fur Color'],
                   location = item['Location'],
                   specific_location = item['Specific Location'],
                   running = b[0],
                   chasing = b[1],
                   climbing = b[2],
                   eating = b[3],
                   foraging = b[4],
                   other_activities = item['Other Activities'],
                   kuks = b[5],
                   quaas = b[6],
                   moans = b[7],
                   tail_flags = b[8],
                   tail_twitches = b[9],
                   approaches = b[10],
                   indifferent = b[11],
                   runs_from = b[12]
            )
            s.save()




