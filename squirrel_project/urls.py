from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list),
    path('stats/', views.squirrel_stats),
]
