from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('logreg', views.loginOrRegister),
    path('success', views.welcomeBooks),
    
    path('addBook', views.addBook),

    path('cleanSession', views.cleanTheSession),

]