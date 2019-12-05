from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list),
    path("<unique_squirrel_id>/", views.edit),
    path("add", views.add)
]
