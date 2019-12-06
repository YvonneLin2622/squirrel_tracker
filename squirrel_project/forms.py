from .models import Squirrel
from django.forms import ModelForm,DateInput

class DateInput(DateInput):
    input_type = 'date'

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ('x','y','unique_squirrel_id','shift',"age","primary_fur_color","location","specific_location","running",'date',"chasing","climbing","eating","foraging","other_activities","kuks","quaas","moans","tail_flags","tail_twitches","approaches","indifferent","runs_from" )
        widgets = {
            'date': DateInput(),
        }

class EditSquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ('x','y','shift',"age","primary_fur_color","location","specific_location","running","date","chasing","climbing","eating","foraging","other_activities","kuks","quaas","tail_flags","tail_twitches","approaches","indifferent","runs_from" )

