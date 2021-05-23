from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('inputsql', views.inputsql),
    path('clear', views.clear),
]