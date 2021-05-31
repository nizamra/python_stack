from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('logreg', views.loginOrRegister),
    path('thoughts', views.welcomeThoughts),
    
    path('addThought', views.addThought),

    path('cleanSession', views.cleanTheSession),

]