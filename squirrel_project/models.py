from django.db import models

class Squirrel(models.Model):
    X = models.DecimalField(
            max_digits=20, 
            deciman_places=18,
            help_text=_('Longitude coordinate for squirrel sighting point'),
            )
    Y = models.DecimalField(
            max_digits=20, 
            deciman_places=18,
            help_text=_('Latitude coordinate for squirrel sighting point'),
            )   
    
    Unique_Squirrel_ID = models.CharField(
            max_length=20,
            help_text=_('Identification tag for each squirrel sightings'),
            )
    
    Hectare = models.CharField(max_length=3)
    
    Shift = models.CharField(max_length=2)
    
    Data = models.DateField(
            help_text=_('Sighting session day and month'),
            )
    
    Hectare_Squirrel_Number = models.IntegerField()
    
    Age = models.CharField(
            max_length=8,
            )
    
    Primary_Fur_Color = models.CharField(
            max_length=8,
            )
            
    Highlight_Fur_Color = models.CharField(
            max_length=8,
            )
