from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('logreg', views.loginOrRegister),
    path('success', views.successPage),
    path('cleanSession', views.cleanTheSession),

]