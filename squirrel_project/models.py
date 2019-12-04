from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    x = models.DecimalField(
            max_digits=20,
            decimal_places=18,
            help_text=_('Longitude coordinate for squirrel sighting point'),
            blank=True, null=True,
            )
    y = models.DecimalField(
            max_digits=20,
            decimal_places=18,
            help_text=_('Latitude coordinate for squirrel sighting point'),
            blank=True, null=True,
            )   
    
    unique_squirrel_id = models.CharField(
            max_length=20,
            help_text=_('Identification tag for each squirrel sightings'),
            blank=True, null=True,
            )
    
    hectare = models.CharField(
            max_length=3,
            blank=True, null=True,
            )
    
    shift = models.CharField(
            max_length=2,blank=True, null=True,
            )
    
    date = models.DateField(
            help_text=_('Sighting session day and month'),
            blank=True, null=True,
            )
    
    
    hectare_squirrel_number = models.IntegerField(blank=True, null=True,)
    
    age = models.CharField(
            max_length=8,
            blank=True, null=True,
            )
    
    primary_fur_color = models.CharField(
            max_length=8,blank=True, null=True,
            )
            
    highlight_fur_color = models.CharField(
            max_length=8,blank=True, null=True,
            )

    combination_of_primary_and_highlight_color = models.CharField(
            max_length=100,blank=True, null=True,
            )

    color_notes= models.CharField(
            max_length=100,blank=True, null=True,
            )

    location = models.CharField(
            max_length=100,blank=True, null=True,
            )

    above_ground_sighter_measurement = models.CharField(
            max_length=100,blank=True, null=True,
            )

    specific_location = models.CharField(
            max_length=100,blank=True, null=True,
            )

    running = models.BooleanField(blank=True, null=True,)
    
    chasing = models.BooleanField(blank=True, null=True,)

    climbing = models.BooleanField(blank=True, null=True,)

    eating = models.BooleanField(blank=True, null=True,)

    foraging = models.BooleanField(blank=True, null=True,)

    other_activities = models.CharField(
            max_length=200,blank=True, null=True,
            )

    kuks = models.BooleanField(blank=True, null=True,)

    quaas = models.BooleanField(blank=True, null=True,)

    moans = models.BooleanField(blank=True, null=True,)

    tail_flags = models.BooleanField(blank=True, null=True,)

    tail_twitches = models.BooleanField(blank=True, null=True,)

    approaches = models.BooleanField(blank=True, null=True,)

    indifferent = models.BooleanField(blank=True, null=True,)

    runs_from = models.BooleanField(blank=True, null=True,)

    other_interactions = models.CharField(
            max_length=200,blank=True, null=True,
            )
    
    lat_long = models.CharField(
            max_length=500,blank=True, null=True,
            )
    zip_codes = models.CharField(
            max_length=5,
            blank=True, null=True
            )
    community_districts = models.IntegerField(blank=True, null=True)
    borough_boundaries = models.IntegerField(blank=True, null=True)
    city_council_districts = models.IntegerField(blank=True, null=True)
    police_precincts = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.unique_squirrel_id
