from django.urls import path
from squirrel_project import views

urlpatterns = [
    path("map/",views.map),
    path("sightings/",views.list),
    path("sightings/<"
         "unique_squirrel_id>/",views.edit),
    path("sightings/add",views.add)
]
