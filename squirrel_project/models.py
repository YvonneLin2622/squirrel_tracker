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
     
    shift = models.CharField(
            max_length=2,
            )
    
    date = models.DateField(
            help_text=_('Sighting session day and month'),
             )
        
    age = models.CharField(
            max_length=8,
            )
    
    primary_fur_color = models.CharField(
            max_length=8,
            )

    location = models.CharField(
            max_length=100,
            )

    specific_location = models.CharField(
            max_length=100,
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

    def __str__(self):
        return self.unique_squirrel_id
