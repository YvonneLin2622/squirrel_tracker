from django.shortcuts import render
from .models import Squirrel

def map(request):
    squirrelList=Squirrel.objects.all()
    return render(request, 'squirrel_project/map.html', locals())
