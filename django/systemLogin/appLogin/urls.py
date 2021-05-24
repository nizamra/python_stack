from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('logreg', views.loginOrRegister),
    # path('addingBook', views.addingsomeBook),
    # path('addingAuthor', views.addingNewAuthor),

    # path('clear', views.cleanAll),
]