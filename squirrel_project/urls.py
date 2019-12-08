from django.urls import path
from . import views

urlpatterns = [
    path("sightings/", views.list),
    path("sightings/add/", views.add),
    path("sightings/stats/", views.squirrel_stats),
    path("sightings/<unique_squirrel_id>/", views.edit),
    path("map/", views.map),
]
