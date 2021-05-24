from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('logreg', views.loginOrRegister),

    # path('cleanData', views.cleanAllData),
    path('cleanSql', views.cleanAllSql),
    path('cleanSession', views.cleanTheSession),

    # path('addingBook', views.addingsomeBook),
    # path('addingAuthor', views.addingNewAuthor),

]