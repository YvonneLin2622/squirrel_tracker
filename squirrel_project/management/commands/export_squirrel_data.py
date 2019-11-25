class Command(BaseCommand):
    help = 'Export Squirrel Data in CSV format'

    def add_arguments(self, parser):
        parser.add_argument('file path', type=str, nargs='+', help='Indicates file path.')

    def handle(self, *args. **kwargs):

