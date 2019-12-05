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

    running = models.BooleanField()

    chasing = models.BooleanField()

    climbing = models.BooleanField()

    eating = models.BooleanField()

    foraging = models.BooleanField()

    other_activities = models.CharField(
            max_length=200,blank=True, null=True,
            )

    kuks = models.BooleanField()

    quaas = models.BooleanField()

    moans = models.BooleanField()

    tail_flags = models.BooleanField()

    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()

    indifferent = models.BooleanField()

    runs_from = models.BooleanField()
    
    def __str__(self):
        return self.unique_squirrel_id
