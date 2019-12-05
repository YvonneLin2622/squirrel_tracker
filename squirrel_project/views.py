from django.shortcuts import render,redirect
from .models import Squirrel
from .forms import SquirrelForm,EditSquirrelForm

def map(request):
    squirrelList=Squirrel.objects.all()
    return render(request, 'squirrel_project/map.html', locals())


def list(request):
    squirrelList=Squirrel.objects.all()
    return render(request, 'squirrel_project/list.html', locals())


def edit(request,unique_squirrel_id):
    squirrel=Squirrel.objects.filter(unique_squirrel_id=unique_squirrel_id).first()
    if request.method == "POST":
        form_obj = EditSquirrelForm(request.POST, instance=squirrel)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/sightings")
    form = EditSquirrelForm(instance=squirrel)
    return render(request, 'squirrel_project/edit.html', {'form': form})

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            Squirrel.objects.create(**form.cleaned_data)
            return redirect("/sightings")
    form = SquirrelForm()
    return render(request, 'squirrel_project/add.html', {'form': form})

