from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('formdata', views.indixingTheSql),
    path('get/<int:num>', views.hisname),
]