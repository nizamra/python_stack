from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('blogs', views.root),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<number>', views.show),
    path('blogs/<number>/edit', views.edit),
    path('blogs/<number>/delete', views.destroy),
    path('time', views.time),
]