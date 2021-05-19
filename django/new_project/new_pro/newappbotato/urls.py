from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('blogs', views.root),
    path('blogs/new', views.new),
    path('blogs/<str:name>', views.name),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('time', views.time),
    path('form', views.form),
    path('result', views.result),
    path('secondform', views.secondform),
    path('counter', views.countthem),
    path('showdata', views.showdata),
    path('destroy_session', views.destroy)
]