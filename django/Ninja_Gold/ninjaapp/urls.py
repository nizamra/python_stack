from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('findGold', views.howMuchGold),
    path('startover', views.clarity),
    path('index2', views.index2),

]