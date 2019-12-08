from django.shortcuts import render,redirect
from .models import Squirrel
from .forms import SquirrelForm
from django.http import HttpResponse

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
            return redirect(f"/sightings/{unique_squirrel_id}")
    form = SquirrelForm(instance=squirrel)
    return render(request, 'squirrel_project/edit.html', {'form': form})


def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings")
    form = SquirrelForm()
    return render(request, 'squirrel_project/add.html', {'form': form})


def squirrel_stats(request):
    squirrelList=Squirrel.objects.all()
    total_num = len(squirrelList)
    avg_x = sum([s.x for s in squirrelList])/total_num
    avg_y = sum([s.y for s in squirrelList])/total_num
    center = (avg_x, avg_y)
    adults_num = sum([1 if s.age == 'Adult' else 0 for s in squirrelList])
    juvenile_num = sum([1 if s.age == 'Juvenile' else 0 for s in squirrelList])
    running_num = sum([1 if s.running  else 0 for s in squirrelList])
    chasing_num = sum([1 if s.chasing  else 0 for s in squirrelList])
    climbing_num = sum([1 if s.climbing  else 0 for s in squirrelList])
    eating_num = sum([1 if s.eating  else 0 for s in squirrelList])
    foraging_num = sum([1 if s.foraging else 0 for s in squirrelList])
    response_text =f"""
    General Statistics about the Sightings:\n\
    Total Number of Squirrels in the sightings: {total_num}\n\
    Center(average longitude and latitude): ({avg_x}, {avg_y})\n\
    Total Number of Adult Squirrels: {adults_num}\n\
    Total Number of Juvenile Squirrels: {juvenile_num}\n\
    Activities of Squirells:\n\
        {running_num} running\n\
        {chasing_num} chasing\n\
        {climbing_num} climbing\n\
        {eating_num} eating\n\
        {foraging_num} foraging\n\
    """
    return HttpResponse(response_text,content_type="text/plain")

