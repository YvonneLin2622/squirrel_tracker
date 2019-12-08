from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list),
    path("add", views.add),
    path('stats/', views.squirrel_stats),
    path("<unique_squirrel_id>/", views.edit),
]
