from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list),
<<<<<<< HEAD
    path("add", views.add),
    path("<unique_squirrel_id>/", views.edit),
=======
    path('stats/', views.squirrel_stats),
>>>>>>> 82b12596bdf6d7c2207a78c59ead0cc530f829b1
]
