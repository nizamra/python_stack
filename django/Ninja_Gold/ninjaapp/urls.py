from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('find', views.find),
    path('index2', views.index2),

]