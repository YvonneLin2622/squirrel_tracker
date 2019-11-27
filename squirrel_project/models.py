from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    x = models.DecimalField(
            max_digits=20,
            decimal_places=18,
            help_text=_('Longitude coordinate for squirrel sighting point'),
            )
    y = models.DecimalField(
            max_digits=20,
            decimal_places=18,
            help_text=_('Latitude coordinate for squirrel sighting point'),
            )   
    
    unique_squirrel_id = models.CharField(
            max_length=20,
            help_text=_('Identification tag for each squirrel sightings'),
            )
    
    hectare = models.CharField(
            max_length=3,
            )
    
    shift = models.CharField(
            max_length=2,
            )
    
    date = models.DateField(
            help_text=_('Sighting session day and month'),
            )
    
    hectare_squirrel_number = models.IntegerField()
    
    age = models.CharField(
            max_length=8,
            )
    
    primary_fur_color = models.CharField(
            max_length=8,
            )
            
    highlight_fur_color = models.CharField(
            max_length=8,
            )

    combination_of_primary_and_highlight_color = models.CharField(
            max_length=100,
            )

    color_notes= models.CharField(
            max_length=100,
            )

    location = models.CharField(
            max_length=100,
            )

    above_ground_sighter_measurement = models.CharField(
            max_length=100,
            )

    specific_location = models.CharField(
            max_length=100,
            )

    running = models.BooleanField()
    
    chasing = models.BooleanField()

    climbing = models.BooleanField()

    eating = models.BooleanField()

    foraging = models.BooleanField()

    other_activities = models.CharField(
            max_length=200,
            )

    kuks = models.BooleanField()

    quaas = models.BooleanField()

    moans = models.BooleanField()

    tail_flags = models.BooleanField()

    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()

    indifferent = models.BooleanField()

    runs_from = models.BooleanField()

    other_interactions = models.CharField(
            max_length=200,
            )
    
    lat_long = models.CharField(
            max_length=500,
            )
    zip_codes = models.CharField(
            max_length=5,
            blank=True, null=True,
            )
    community_districts = models.IntegerField(blank=True, null=True)
    borough_boundaries = models.IntegerField(blank=True, null=True)
    city_council_districts = models.IntegerField(blank=True, null=True)
    police_precincts = models.IntegerField(blank=True, null=True)

