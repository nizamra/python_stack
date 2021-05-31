from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('logreg', views.loginOrRegister),
    path('thoughts', views.welcomeThoughts),
    
    path('addThought', views.addThought),
    path('likethis/<int:id>', views.likeThought),
    path('unlikethis/<int:id>', views.unlikethisThought),
    path('thought/<int:id>', views.thoughtData),

    path('cleanSession', views.cleanTheSession),

]